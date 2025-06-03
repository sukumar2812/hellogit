import fabric.functions as fn
udf=fn.UserDataFunctions()

@udf.function()
def greetings_message(name: str)->str:
    return f"Hello, {name}"

 