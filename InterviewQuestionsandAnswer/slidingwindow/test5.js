

var test = "test value"

function customfunc()
{
   var test1 = "test1 value"
   return function()
   {
    console.log(test1)
   }
}

customfunc()()

console.log(multiply(2)(3)); // prints 6

function multiply(a)
{
    return function(b)
    {
        return a*b
    }
}

