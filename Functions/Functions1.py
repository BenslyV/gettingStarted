# paint area calculator

print("Welcome to paint Calculator")
height = int(input(f"Enter the height\n"))
width = int(input(f"Enter the width"))


def paint_area(height1=height, width1=width, coverage=5):
    area_painted = int((height * width) / coverage)
    print(f"Paining area would be {area_painted} ")
    return area_painted


paint_area(height, width, 5)