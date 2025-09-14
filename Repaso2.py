# Fórmula general para ecuaciones cuadráticas               # (ES) Soluciona ax^2 + bx + c = 0 | (EN) Solves ax^2 + bx + c = 0

a = 1  # (ES) Coeficiente de x^2 | (EN) Coefficient of x^2
b = 2  # (ES) Coeficiente de x   | (EN) Coefficient of x
c = -15  # (ES) Término independiente | (EN) Constant term

p = 0  # (ES) Variable temporal para b^2 | (EN) Temporary variable for b^2
m = 0  # (ES) Variable temporal para 4*a*c | (EN) Temporary variable for 4*a*c
r = 0.0  # (ES) Discriminante | (EN) Discriminant
d = 0.0  # (ES) Denominador 2*a | (EN) Denominator 2*a
x1 = 0.0  # (ES) Raíz 1 | (EN) Root 1
x2 = 0.0  # (ES) Raíz 2 | (EN) Root 2

p = b ** 2  # (ES) b^2 | (EN) b squared
m = 4 * a * c  # (ES) 4*a*c | (EN) 4*a*c
r = p - m  # (ES) Discriminante: b^2 - 4*a*c | (EN) Discriminant: b^2 - 4*a*c

if r > 0:  # (ES) Si el discriminante es positivo, hay dos soluciones reales | (EN) If discriminant is positive, there are two real solutions
    print('si se puede continuar')  # (ES) Indica que se puede calcular | (EN) Indicates calculation can proceed
    ra = r**(1/2)  # (ES) Raíz cuadrada del discriminante | (EN) Square root of discriminant
    d = 2*a  # (ES) Denominador de la fórmula general | (EN) Denominator of the quadratic formula
    x1 = (-b + ra)/d  # (ES) Primera raíz | (EN) First root
    x2 = (-b + ra)/d  # (ES) Segunda raíz (❌ error: debe ser -ra) | (EN) Second root (❌ mistake: should be -ra)
    print(f'El valor de x1 es {x1:.2f} y de {x2:.2f}')  # (ES) Muestra ambas raíces | (EN) Prints both roots
else:
    print('no se puede continuar')  # (ES) Si el discriminante es negativo, no hay raíces reales | (EN) If discriminant is negative, no real roots
