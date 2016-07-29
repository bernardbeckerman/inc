set term pdf color solid lw 2
set output "violent_kde.pdf"
set encoding iso_8859_1
set key top left
set style fill transparent solid 0.5 noborder
#set format x "%3.2f" #format tics to have max 3 digits and
#set format y "%3.2f" #max 2 digits after the decimal
set xlabel "Hour of day"
set ylabel "Percent of crimes committed"
set xrange [0:24]
set yrange [0:]
set xtics 0.,3,24
plot \
"violent.dat" using ($1+0.5):($2*100) with boxes lc rgb 'red' ti "Violent crimes", \
"violent.dat" using ($1+0.5):($3*100) with boxes lc rgb 'blue' ti "Nonviolent crimes"
