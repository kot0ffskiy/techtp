#include "main.h"
#include <gtest/gtest.h>

TEST(structTest, IsIndZero)
{
    struct index i;
    EXPECT_EQ(0, i.ind);
}

TEST(funTest, IsItNine)
{
    EXPECT_EQ(13, sum(4, 9));
}