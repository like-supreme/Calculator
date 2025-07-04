from art import logo
from operator_functions import adding_op as add
from operator_functions import remove_op as rem
from operator_functions import multiply_op as mul
from operator_functions import divide_op as div 



operators = {
    "+" : add,
    "-" : rem,
    "*" : mul,
    "/" : div
}

def main():
    """Burada yapacağımız şey tanımlanmış fonksiyonları çağırmak kullanıcıya hangi işlemi yapmak istediğini sormak işlemi yapıp ekrana yazdırmak 
    ve ekranı temizlemek"""
    print(logo)
    number1 = float(input("what is your first number. \n"))  
    for symbols in operators:
        print(*symbols)
        
    is_cont = True
    while is_cont is True:
        operator_symbol = input("Pick an operator. Add for + subtract for - multiply for * divide for /. İf you want to exit. Please type stop. \n")
        if operator_symbol == "stop":
            break
        number2 = int(input("What is your second number ? "))
        operator_action = operators[operator_symbol]
        answer = operator_action(number1 , number2)
        print(f"your first number is: {number1}. and your second answer is: {number2}. you selected the {operator_symbol}. Your answer is {answer}")
        y_or_n = input("Wanna continue ? type y for contiune type n for exit ")
        
        if y_or_n == "y":
            is_cont = True
            print("\033c", end="")
            main()
            return
        else: 
            is_cont = False
            print("\033c", end="")
            return

main()
            
        
        
        



        
    

    
        
          