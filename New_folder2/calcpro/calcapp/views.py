from django.shortcuts import render
from django.http import HttpResponse

def demo(request):
    solution = ""

    if request.method == 'POST':
        n1 = eval(request.POST.get("a"))   # ✅ convert
        n2 = eval(request.POST.get("b"))   # ✅ convert
        opr = request.POST.get("opr")

        if opr == "+":
            solution = n1 + n2
        elif opr == "-":
            solution = n1 - n2
        elif opr == "*":
            solution = n1 * n2
        elif opr == "/":
            solution = n1 / n2
        elif opr == "**":
            solution = n1 ** n2

    return render(request, "index.html", {'solution': solution})