def handle_uploaded_file(f):  
    with open('D:/ALIMweb/djangoweb/upload/error/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)

    return f
     