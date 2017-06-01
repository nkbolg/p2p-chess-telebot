#include "DumbDLL.h"

extern "C" bool getPos(int s0, int s1, int e0, int e1)
{
  return s0 + s1 < e0 + e1;
}