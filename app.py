import analysis
import function_menu

def main():
    is_running = True
    rows = analysis.load_sales()
    while is_running:
        function_menu.display_function_menu()
        try:
            choice = input("Select a function ID: ").strip()
            function_str = function_menu.match_function(choice)
            if function_str == function_menu.FUNCTION_DISPLAY_SALES:
                analysis.display_sales(rows)                
            elif function_str == function_menu.FUNCTION_TOTAL_REVENUE:
                revenue = analysis.total_revenue(rows)
                print(f"Total Revenue: ${revenue:,.2f}")
            elif function_str == function_menu.FUNCTION_TOTAL_UNITS:
                total_units = analysis.total_units(rows)
                print(f"Total Units Sold: {total_units}")    
            elif function_str == function_menu.FUNCTION_EXIT:
                is_running = False
                break
        except ValueError:
            print("Invalid choice. Enter a number.")
            continue


if __name__ == "__main__":
    main()
