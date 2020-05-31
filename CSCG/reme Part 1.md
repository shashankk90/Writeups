# reme Part 1
**Category:** Reverse Engineering  
**Difficulty:** Easy  
**Author:** 0x4d5a  

>.NET Reversing can't be that hard, right? But I've got some twists waiting for you 😈
Execute with .NET Core Runtime 2.2 with windows, e.g. dotnet ReMe.dll

## Solution
When we open the _dll_ file with dnSpy, we can basically see what the code was(almost). The program takes an argument and compares it with the password(or flag). But the password is stored in encrypted form. It is decrypted and then compared with passed argument.
```csharp
bool flag5 = args[0] != StringEncryption.Decrypt("D/T9XRgUcKDjgXEldEzeEsVjIcqUTl7047pPaw7DZ9I=");
if (flag5)
{
	Console.WriteLine("Nope");
	Environment.Exit(-1);
}
else
{
	Console.WriteLine("There you go. Thats the first of the two flags! CSCG{{{0}}}", args[0]);
}
```
dnSpy can be used to edit the code directly. So instead of printing "Nope" when the check fails, we will print the flag.
```csharp
if (args[0] != StringEncryption.Decrypt("D/T9XRgUcKDjgXEldEzeEsVjIcqUTl7047pPaw7DZ9I="))
{
	Console.WriteLine(StringEncryption.Decrypt("D/T9XRgUcKDjgXEldEzeEsVjIcqUTl7047pPaw7DZ9I="));
	Environment.Exit(-1);
}
else
{
	Console.WriteLine("There you go. Thats the first of the two flags! CSCG{{{0}}}", args[0]);
}
```
Now if we run the dll file, we will get the flag
```
dotnet ReMe.dll AAAA
CanIHazFlag?
```
### CSCG{CanIHazFlag?}
