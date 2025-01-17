; ModuleID = "/Users/maksimalsevskih/Downloads/IU7/IU7sem2/compiler/Kurs_work/llvm_file.py"



@"fstr" = internal constant [5 x i8] c"%d \0a\00"
declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"res" = mul i32 10, 5
  %".2" = bitcast [5 x i8]* @"fstr" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %"res")
  ret i32 %"res"
}

@"fstr" = internal constant [5 x i8] c"%d \0a\00"
declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"res" = add i32 i, 1
  %".2" = bitcast [5 x i8]* @"fstr" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %"res")
  ret i32 %"res"
}
