// Fibonacci Moving Averages 
// @version=4
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © savagezen

study(title="Fibonacci Moving Averages", shorttitle="MA-FBNCI", overlay=true)

// yearly average
len = input(377, minval=1, title="Length")
src = input(close, title="Source")
out = sma(src, len)

// quarterly average
len2 = input(89, minval=1, title="Length")
src2 = input(close, title="Source")
out2 = sma(src2, len2)

// monthly average
len3 = input(34, minval=1, title="Length")
src3 = input(close, title="Source")
out3 = sma(src3, len3)

// weekly average
len4 = input(8, minval=1, title="Length")
src4 = input(close, title="Source")
out4 = sma(src4, len4)

// plots
plot(out, color=#2ef538, title="MA377") //lime - yearly=
plot(out2, color=#f52e87, title="MA089") //pink - quarterly
plot(out3, color=#2eebf5, title="MA034") //cyan - monthly
plot(out4, color=#ebf52e, title="MA008") //yellow - weekly

//Adapted from "Moving Averages 50 & 200" by Mobitz
