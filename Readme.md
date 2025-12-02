def add(request):
    # a = input("Enter your frist name:")
    # b = input("Enter you last name:")

    # return HttpResponse(f"<h1>{a} {b}</h1>")

    result = None
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')

        result = int(num1) + int(num2)

    return render(request, "add.html", {"result":result})
    ---------------------------------------------------------------------------
    
# there we go--- WO HOOO!

