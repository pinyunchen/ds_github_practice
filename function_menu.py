
FUNCTION_DISPLAY_SALES = "Display Sales"
FUNCTION_TOTAL_REVENUE = "Total Revenue"
FUNCTION_TOTAL_UNITS = "Total Units"
FUNCTION_EXIT = "Exit"

FUNCTION_MENU = {
    "1": FUNCTION_DISPLAY_SALES,
    "2": FUNCTION_TOTAL_REVENUE,
    "3": FUNCTION_TOTAL_UNITS,
    "0": FUNCTION_EXIT,
}

def match_function(choice):
    function_str = ""
    if choice in FUNCTION_MENU:
        function_str = FUNCTION_MENU[choice]
    return function_str

def display_function_menu():
    print("\nAnalysis Functions")
    for id, function_str in FUNCTION_MENU.items():
        print(f"[{id}] {function_str}")
   
def show_welcome_message(_rows):
    print("Welcome to the Sales Analysis Tool.")

