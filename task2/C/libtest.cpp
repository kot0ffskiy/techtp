#include "main.h"
#include <gtest/gtest.h>

TEST(structTest, IsIndZero)
{
    struct index i;
    EXPECT_EQ(0, i.ind);
}

TEST(funTest, IsItNine)
{
    EXPECT_EQ(13, summa(4, 9));
}