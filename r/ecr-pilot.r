#!/usr/bin/R
# ECR-4 Pilot

# correlation
# cor(x, y, method="pearson")
# method can be pearson or spearman

case <- c('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19')
age <- c(14, 16, 16, 17, 14, 13, 13, 14, 15, 13, 12, 12, 11, 12, 9, 11, 14, 16, 17)
gender_m <- c(FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, TRUE, FALSE, FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE, FALSE, TRUE)
race_w <- c(TRUE, TRUE, TRUE, TRUE, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, TRUE, FALSE, TRUE, TRUE, TRUE, TRUE)
dx_bp <- c()
dx_mdd <- c(FALSE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, TRUE, TRUE, TRUE, TRUE, FALSE, TRUE, TRUE, TRUE, FALSE, FALSE)
dx_ptsd <- c(TRUE, FALSE, FALSE, TRUE, TRUE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE)
dx_adhd <- c()
dx_sa <- c(FALSE, FALSE, FALSE, TRUE, FALSE, FALSE, FALSE, TRUE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE)
dx_gad <- c(FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, FALSE, FALSE, TRUE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, TRUE, FALSE)
dx_odd <- c(FALSE, TRUE, FALSE, FALSE, FALSE, TRUE, FALSE, FALSE, FALSE, TRUE, FALSE, FALSE, FALSE, TRUE, FALSE, FALSE, FALSE, FALSE, TRUE)
dx_ied <- c(FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, TRUE, FALSE, FALSE, TRUE, FALSE, FALSE, FALSE, FALSE)
rx_ax <- c(1, -9, -3, -2, 1, -3, 0, 3, -2, 5, -3, 3, 1, -5, -8, -5, -3, 2, -3)
rx_avd <- c(-5, -3, 1, 2, 11, 5, 2, 3, 8, -3, -3, -9, -5, 1, 4, -7, -5, 10, 3)
atch_fearful <- c()
atch_dismissive <- c()
atch_secure <- c()
atch_prpeoccupiped <- c()

cat("Correlations:\n")

cat("\tAge and Anxiety")
cor(age, rx_ax, method="pearson")
chisq.test(age, rx_ax)
cat("\n")

cat("\tAge and Avoidance")
cor(age, rx_avd, method="pearson")
chisq.test(age, rx_avd)
cat("\n")

cat("\tGender and Anxiety")
cor(gender_m, rx_ax, method="pearson")
chisq.test(gender_m, rx_ax)
cat("\n")

cat("\tGender and Avoidance")
cor(gender_m, rx_avd, method="pearson")
chisq.test(gender_m, rx_avd)
cat("\n")

cat("\tRace and Anxiety")
cor(race_w, rx_ax, method="pearson")
chisq.test(race_w, rx_ax)
cat("/n")

cat("\tRace and Avoidance")
cor(race_w, rx_avd, method="pearson")
chisq.test(race_w, rx_avd)
cat("\n")

cat("\tBipolar and Anxiety")
#cor(dx_bp, rx_ax, method="pearson")
cat("\tBipolar and Avoidance")
#cor(dx_bp, rx_avd, method="pearson")
cat("\n")

cat("\tMDD and Anxiety")
cor(dx_mdd, rx_ax, method="pearson")
cat("\tMDD and Avoidance")
cor(dx_mdd, rx_avd, method="pearson")
cat("\n")

cat("\tPTSD and Anxiety")
cor(dx_ptsd, rx_ax, method="pearson")
cat("\tPTSD and Avoidance")
cor(dx_ptsd, rx_avd, method="pearson")
cat("\n")

cat("\tADHD and Anxiety")
#cor(dx_adhd, rx_ax, method="pearson")
cat("\tADHD and Avoidance")
#cor(dx_adhd, rx_avd, method="pearson")
cat("\n")

cat("\tSubstance Abuse and Anxiety")
cor(dx_sa, rx_ax, method="pearson")
cat("\tSubstance Abuse and Avoidance")
cor(dx_sa, rx_avd, method="pearson")
cat("\n")

cat("\tGAD and Anxiety")
cor(dx_gad, rx_ax, method="pearson")
cat("\tGAD and Avoidance")
cor(dx_gad, rx_avd, method="pearson")
cat("\n")

cat("\tODD and Anxiety")
cor(dx_odd, rx_ax, method="pearson")
cat("\tODD and Avoidance")
cor(dx_odd, rx_avd, method="pearson")
cat("\n")

cat("\t IED and Anxiety")
cor(dx_ied, rx_ax, method="pearson")
cat("\t IED and Avoidance")
cor(dx_ied, rx_avd, method="pearson")
