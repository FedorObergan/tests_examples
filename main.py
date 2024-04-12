import math




def perimeter_and_area_of_rectangle(a, b):
    if a>0 and b>0:
        perimeter = 2*(a+b)
        area = a*b
        return {'perimeter': perimeter,
                'area': area}
    else:
        return {'perimeter': -1,
                'area': -1}


def pairing_boys_and_girls_after_sorting(boys: list, girls: list):
    result = ""
    if len(boys) == len(girls):
        boys.sort()
        girls.sort()
        for elem in zip(boys, girls):
            result += f"{elem[0]} и {elem[1]}, "
        result = result.strip(", ")
    else:
        result = "Кто-то может остаться без пары!"
    return result


def discriminant(a, b, c):
  return b**2 - 4*a*c


def solution_of_quadratic_equation(a, b, c):
  if(discriminant(a, b, c) < 0):
      return "вещественных корней нет"
  elif(discriminant(a, b, c) == 0):
      return f"{-b/(2*a)}"
  else:
      return f"{(-b + math.sqrt(discriminant(a, b, c)))/(2*a)} {(-b - math.sqrt(discriminant(a, b, c)))/(2*a)}"

