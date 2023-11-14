import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--funckja', type=str, required=True, help="Funkcja np. x**2+x+1")
parser.add_argument('-s',"--start", type=float, help="punkt startowy")
parser.add_argument('-d',"--dlugosc", type=float, help="wielskosc kroku w pochodnej")
parser.add_argument('-k',"--kroki", type=int, help="ilosc krokow metody")
parser.add_argument('-t',"--torelancja", type=float, help="dokladnosc, np. 1e-6")
args = parser.parse_args()

def newton_method(func,initial_guess, alpha, max_iterations, tolerance):
    
    x = initial_guess
    iteration = 0

    while iteration < max_iterations:
        f_x = eval(func, {'x': x}) 
        f_prime_x =(eval(func, {'x': x + tolerance}) - f_x) / tolerance
        if abs(f_x) < tolerance:
            break

        x = x - f_x / f_prime_x
        iteration += 1

    return x

def main():
    initial_guess=args.start
    alpha = args.dlugosc
    max_iterations = args.kroki
    tolerance = args.torelancja
    func = args.funckja
    print(newton_method(func, initial_guess,alpha,max_iterations,tolerance))
if __name__ == '__main__':
    main()

