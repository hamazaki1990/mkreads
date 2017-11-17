import subprocess


for i in range(1,10):
    inputfastq1 = "%s_D1Z5_peri3_artificial_shortread_1.fastq" %i
    inputfastq2 = "%s_D1Z5_peri3_artificial_shortread_2.fastq" %i
    outputsam = "%s_D1Z5artificial3_DXZ1HOR.sam" %i
    alconcfastq = str(i)+"_D1Z5artificial3_DXZ1HOR_al_conc_%.fastq"
    subprocess.run(["bowtie2", "-x", "2times_DXZ1_HOR", "-1", inputfastq1, "-2", inputfastq2, "-S", outputsam, "--al-conc", alconcfastq])




