import classes  #importing 'classes.py' will set its __name__ to 'classes', making the condition (if __name__ == '__main__') false.
classes.main() #despite the function not being executed on import, we can still run it by calling it by name

print(f"Modules Name: {__name__}") #since the file 'modules.py' is run directly, its __name__ is set to __main__
