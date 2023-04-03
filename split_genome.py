#!/usr/bin/env python

from Bio import SeqIO as SIO
import os
import glob
from multiprocessing import Pool

genomedir = "/Users/suzukiyuuta/working/cns/split_genome/"
ensemblplant = "/Users/suzukiyuuta/db/ensemblplant/*.fa"


def split_genome(genome,spices_name):	
	#make directory
	outdir = genomedir + spices_name
	try:
		os.makedirs(outdir)
	except FileExistsError :
		return
	#make split genome
	records_dict = SIO.index(genome,"fasta")
	for recrod_id, record in records_dict.items():
		if not record.id.startswith(tuple(map(str, range(10)))):
			continue
		outfile = os.path.join(outdir,spices_name + '_' + record.id + '.fa')
		SIO.write(record, outfile, 'fasta')
	return

def get_name(path):
	fasta_file = os.path.basename(path)
	spices_name = fasta_file.split(".")[0]
	return spices_name

if __name__ == '__main__':
	p_genome = glob.glob(ensemblplant)
	li_spices = list(map(get_name,p_genome))
	for_map = list(zip(p_genome,li_spices))
	with Pool(4) as p :
		p.starmap(split_genome,for_map)




