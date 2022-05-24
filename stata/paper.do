******************************

*Variable initialization

gen lnAge = log(live_year+1)
gen lnDigitalInvest = log(digitalinvest+1)
gen lnBigdata = log(bigdata+1)
gen lnEdu = log(edu+1)
gen lniv = log(iv)
gen roa = roa_val*100
gen lnAssets = log(assets)
encode industry, gen(industry_en)
encode area,gen(area_en)
winsor2 lnDigitalInvest, replace cuts(1 99)
winsor2 lnEdu, replace cuts(1 99)
winsor2 lnAge, replace cuts(1 99)
winsor2 lnAssets, replace cuts(1 99)
winsor2 PPE_TA, replace cuts(1 99)
winsor2 roa, replace cuts(1 99)

sum lnEdu lnAge lnAssets PPE_TA lnDigitalInvest lniv roa

***********************************************  **



**********Control Variable*************************

glob Control lnEdu lnAge lnAssets PPE_TA

************************************************


************************The relationship of lnDigitalInvest with lnBigdata***************************

reghdfe lnDigitalInvest lnBigdata,absorb(ts_code area_en industry_en) vce(cluster ts_code)
est store s1
esttab s1 using lnBigdata_lnDigitalInvest.rtf,se(3) noconstant star(* 0.1 ** 0.05 *** 0.01)

*****************************************************************************



**********************The relationship of lnDigitalInvest with Control Variable***************************

reghdfe lnDigitalInvest $Control,absorb(ts_code area_en industry_en) vce(cluster ts_code)
est store s2
esttab s2 using lnDigitalInvest_Control.rtf,se(3) noconstant star(* 0.1 ** 0.05 *** 0.01)


***************************************************************************



***************************The relationship of roa with lnDigitalInvest in different cluster*****************************

reghdfe roa lnDigitalInvest $Control,absorb(ts_code area_en industry_en) vce(cluster ts_code)
est store m1
reghdfe roa lnDigitalInvest $Control,absorb(ts_code industry_en) vce(cluster ts_code)
est store m2
reghdfe roa lnDigitalInvest $Control,absorb(ts_code area_en) vce(cluster ts_code)
est store m3
reghdfe roa lnDigitalInvest $Control,absorb(ts_code) vce(cluster ts_code)
est store m4
esttab m1 m2 m3 m4 using roa_different_effiection.rtf,se(3) noconstant star(* 0.1 ** 0.05 *** 0.01)

*******************************************************************************



***************************IV Control Variable************************************************

ivreghdfe roa $Control (lnDigitalInvest=lniv), absorb(ts_code industry_en) cluster(ts_code) first
est store iv_without_area

esttab iv_without_area using roa_iv.rtf,se(3) noconstant star(* 0.1 ** 0.05 *** 0.01)


ivreghdfe roa $Control (lnDigitalInvest=lniv), absorb(ts_code area_en industry_en) cluster(ts_code) first
est store iv_with_area

esttab iv_with_area using roa_iv.rtf,se(3) noconstant star(* 0.1 ** 0.05 *** 0.01)


************************************************************************************************