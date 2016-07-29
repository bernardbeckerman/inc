set title "Percent of violent crimes vs. time committed" font ",12"
set term pdf color solid lw 2
ystr = "2017"
set output sprintf("freq_polar_%s.pdf",ystr)
set encoding iso_8859_1
set key top left
set style fill transparent solid 0.5 noborder
#set format x "%3.2f" #format tics to have max 3 digits and
#set format y "%3.2f" #max 2 digits after the decimal
set polar
#set tlabel "Hour of day"
#set rlabel "Percent of crimes committed"
set size square
set trange [0:2*pi]
set rrange [0:7]
#set xtics 0.,3,24
set grid polar pi/12
set view equal xy
set noxtics
set noytics
set rtics 2 format '' scale 0
p4=pi/4
set style data impulse
delta = 0.025
pol_label(x, text) = sprintf("set label '%s' at (6.7*cos(0.5*pi-%f)), (6.7*sin(0.5*pi-%f))     center", text, x, x)
eval pol_label(0*p4, "0h")
eval pol_label(1*p4, "3h")
eval pol_label(2*p4, "6h")
eval pol_label(3*p4, "9h")
eval pol_label(4*p4, "12h")
eval pol_label(5*p4, "15h")
eval pol_label(6*p4, "18h")
eval pol_label(7*p4, "21h")

rad_label(x, text) = sprintf("set label '%s%%' at 0.2,%f", text, x+0.25)
#eval rad_label(2, '2')
eval rad_label(4, '4')
eval rad_label(6, '6')
#eval rad_label(40, '40')
unset raxis
unset border

plot \
sprintf("prd_vm%s.dat",ystr) using (0.5*pi-($1)/12*pi+delta):($2*100*pi/12.0) w lines lc rgb 'red' ti ystr, \

#plot \
#"violent.dat" using (0.5*pi-$1/12*pi+delta):($2*100) lw 3 lc rgb 'red' ti "Violent", \
#"prd_vm.dat" using (0.5*pi-($1)/12*pi+delta):($2*100*pi/12.0) w lines lc rgb 'red' noti, \
#"violent.dat" using (0.5*pi-$1/12*pi-delta):($3*100) lw 3 lc rgb 'blue' ti "Nonviolent"
