#!/usr/bin/env python
import argparse
import inspect
import json
import sys

import wikipedia_tool


def list_functions(args):
    """
    List all available functions in the wikipedia_tool module.
    If the verbose option is enabled, a brief description of each function is displayed.
    """
    funcs = [f for f in inspect.getmembers(wikipedia_tool, inspect.isfunction) if not f[0].startswith("_")]
    if args.verbose:
        for name, func in funcs:
            doc_line = func.__doc__.strip().splitlines()[0] if func.__doc__ else ""
            print(f"{name}: {doc_line}")
    else:
        for name, _ in funcs:
            print(name)


def help_function(args):
    """
    Display the documentation (docstring) of a specified function.
    
    Args:
        args.function (str): The name of the function.
    
    Output:
        Prints the function's documentation if available.
    """
    func = getattr(wikipedia_tool, args.function, None)
    if not func:
        print(f"Function '{args.function}' not found.")
        sys.exit(1)
    doc = inspect.getdoc(func)
    print(doc if doc else "No documentation available.")


def run_function(args):
    """
    Execute a specified function with provided key=value parameters.
    
    Args:
        args.function (str): The function name to execute.
        args.params (list): A list of parameters in key=value format.
    
    Output:
        Prints the result of the function if any.
    """
    func = getattr(wikipedia_tool, args.function, None)
    if not func:
        print(f"Function '{args.function}' not found.")
        sys.exit(1)

    sig = inspect.signature(func)
    kwargs = {}

    for kv in args.params:
        if "=" not in kv:
            print(f"Invalid parameter format: {kv}. Use key=value.")
            sys.exit(1)
        key, value = kv.split("=", 1)
        try:
            converted = json.loads(value)
        except Exception:
            converted = value
        kwargs[key] = converted

    try:
        result = func(**kwargs)
        if result is not None:
            print(result)
    except Exception as e:
        print(f"Error executing function: {e}")
        sys.exit(1)


def main():
    """
    Main CLI entry point for the wikipedia_tool command-line interface.
    
    Available subcommands:
      - list: Display all available functions in the module.
      - help: Show documentation for a specific function.
      - run: Execute a function with key=value arguments.
    """
    parser = argparse.ArgumentParser(
        description="Advanced CLI for wikipedia_tool with support for 300+ API options",
        epilog="Use 'list', 'help', or 'run' subcommands. Example:\n"
               "  - list [-v]\n"
               "  - help <function_name>\n"
               "  - run <function_name> key1=value1 key2=value2 ..."
    )
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand", required=True)

    list_parser = subparsers.add_parser("list", help="List all available functions")
    list_parser.add_argument("-v", "--verbose", action="store_true", help="Show brief descriptions of functions")
    list_parser.set_defaults(func=list_functions)

    help_parser = subparsers.add_parser("help", help="Show documentation for a specific function")
    help_parser.add_argument("function", help="Function name")
    help_parser.set_defaults(func=help_function)

    run_parser = subparsers.add_parser("run", help="Execute a function with key=value parameters")
    run_parser.add_argument("function", help="Function name")
    run_parser.add_argument("params", nargs="*", help="Parameters in key=value format")
    run_parser.set_defaults(func=run_function)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
