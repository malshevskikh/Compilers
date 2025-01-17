; ModuleID = "/Users/maksimalsevskih/Downloads/IU7/IU7sem2/compiler/Kurs_work/llvm_file_complex_math.py"


@"fstr" = internal constant [5 x i8] c"%d \0a\00"
declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"res" = add i32 4, 6
  %"res.1" = sdiv i32 %"res" = add i32 4, 6, 2
  %".2" = bitcast [5 x i8]* @"fstr" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %"res.1")
  ret i32 %"res.1"
}

@"fstr" = internal constant [5 x i8] c"%d \0a\00"
declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"res" = add i32 4, 6
  %"res.1" = sdiv i32 %"res" = add i32 4, 6, 2
  %".2" = bitcast [5 x i8]* @"fstr" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %"res.1")
  ret i32 %"res.1"
}
