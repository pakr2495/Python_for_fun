b = 30
function fristfunc()
{
    let a = 2
    function secnodfunc()
    {
        a= a+10
        console.log(a)
        console.log(b)
        b= b+50
    }
    a = a+ 10
    return secnodfunc
}


a1 = fristfunc()
a1()
b = b + 30
a1()
