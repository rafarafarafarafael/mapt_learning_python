def func1():
    print('function 1')
    def func2():
        print('function 2')
    func2()
    
func1()
func1.func2()
