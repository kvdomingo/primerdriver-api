from .primerclass import *
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord

def singleCommand_handler(args):
    args_dict = dict()
    args_dict['mode'] = args.mode
    if args.mode.upper() =='DNA':
        args_dict['sequence'] = args.sequence
        PrimerChecks(args.sequence).check_sequence_length()
        PrimerChecks(args.sequence).check_valid_base()
        args_dict['mutation_type'] = args.mutation_type
        args_dict['position'] = args.position
        args_dict['destination'] = args.destination
        if args.mutation_type.upper() in ['S', 'SUB']:
            args_dict['target'] = args.target
        else:
            raise ValueError("Invalid argument passed to 'MUTATION_TYPE'")
    elif args.mode.upper() == 'CHAR':
        if args.sequence.endswith('.txt'):
            with open(args.sequence, 'r', encoding='utf-8') as f:
                args_dict['sequence'] = f.read().strip()
        elif args.sequence.endswith('.fasta'):
            with open(args.sequence, 'r', encoding='utf-8') as f:
                args_dict['sequence'] = list(SeqIO.parse(f, 'fasta'))[0].seq.strip()
        else:
            args_dict['sequence'] = args.sequence
        PrimerChecks(args.sequence).check_valid_base()
        args_dict['mutation_type'] = args.mutation_type
        args_dict['mismatched_bases'] = args.position
    else:
        raise NotImplementedError(f"{args_dict['mode']} mode not implemented (yet).")
    return args_dict

def interactive_handler():
    args_dict = dict()
    print('')
    print('====================================')
    print('======                        ======')
    print('===     PrimerDriver v0.1.2      ===')
    print('======                        ======')
    print('====================================\n')
    print('(c) 2020 Kenneth Domingo & Nomer Gutierrez\n')
    args_dict['mode'] = input('Enter primer mode [dna/pro/char]: ')
    if args_dict['mode'].upper() == 'DNA':
        args_dict['sequence'] = input('Enter DNA sequence: ')
        PrimerChecks(args_dict['sequence']).check_sequence_length()
        PrimerChecks(args_dict['sequence']).check_valid_base()
        args_dict['mutation_type'] = input('Enter mutation type [s/i/d]: ')
        if args_dict['mutation_type'].upper() in ['S', 'SUB']:
            args_dict['target'] = input('Enter target base: ')
            args_dict['destination'] = input('Enter replacement for target base: ')
            args_dict['position'] = int(input('Enter position of target: '))
        elif args_dict['mutation_type'].upper() in ['I', 'INS']:
            args_dict['target'] = None
            args_dict['destination'] = input('Enter insertion sequence: ')
            args_dict['position'] = int(input('Enter insertion position: '))
        elif args_dict['mutation_type'].upper() in ['I', 'INS']:
            args_dict['target'] = None
            args_dict['destination'] = input('Enter starting position to delete: ')
        else:
            raise ValueError("Invalid argument passed to 'MUTATION_TYPE'")
    elif args_dict['mode'].upper() == 'CHAR':
        args_dict['sequence'] = input('Enter primer sequence: ')
        args_dict['mutation_type'] = input('Enter mutation type [s/i/d]: ')
        args_dict['mismatched_bases'] = input('Enter number of mismatched bases: ')
    else:
        raise NotImplementedError(f"{args_dict['mode']} mode not implemented (yet).")

    return args_dict