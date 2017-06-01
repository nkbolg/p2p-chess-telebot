#ifndef DumbDLL_h__
#define DumbDLL_h__


#ifdef DUMBDLL_EXPORTS
#define DUMBDLL_API __declspec(dllexport)
#else
#define DUMBDLL_API __declspec(dllimport)
#endif


extern "C" bool DUMBDLL_API getPos(int s0, int s1, int e0, int e1);


#endif // DumbDLL_h__
