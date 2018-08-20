import os
import glob
import argparse 

from submitLHECondorJob import submitCondorJob

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('proc', help="Name of physics model")
    parser.add_argument('--cards-dir', dest='cardsDir', help="Path to directory with cards", required=True)
    parser.add_argument('--genproductions-dir', dest='genproductionsDir', help='Path to genproductions repository', default='/home/users/'+os.environ['USER']+'/mcProduction/genproductions')
    parser.add_argument('--no-sub', dest='noSub', action='store_true', help='Do not submit jobs')
    parser.add_argument('--proxy', dest="proxy", help="Path to proxy", default=os.environ["X509_USER_PROXY"])
    args = parser.parse_args()

    proc = args.proc
    cards_dir = args.cardsDir
    genproductions_dir = args.genproductionsDir

    script_dir = os.path.dirname(os.path.realpath(__file__))
    executable = script_dir+'/runGridpackGeneration.sh'
    out_dir = '/hadoop/cms/store/user/'+os.environ['USER']+'/mcProduction/GRIDPACKS/'+proc

    #gridpack generation script and misc scripts
    infile_list = [script_dir+'/gridpack_generation.sh'] #use modified gridpack generation script 
    infile_list.append(genproductions_dir+'/bin/MadGraph5_aMCatNLO/runcmsgrid_LO.sh')
    infile_list.append(genproductions_dir+'/bin/MadGraph5_aMCatNLO/cleangridmore.sh')
    #patches needed by gridpack generation script
    #infile_list.append(script_dir+'/ucsd.patch') #use the patch committed in this repository
    infile_list.append(genproductions_dir+'/bin/MadGraph5_aMCatNLO/patches/mgfixes.patch')
    infile_list.append(genproductions_dir+'/bin/MadGraph5_aMCatNLO/patches/models.patch')
    #madgraph cards
    infile_list += glob.glob(cards_dir+'/*.dat')

    if not os.path.isdir("logs/%s"%proc):
        os.makedirs("logs/%s"%proc)

    infile = ','.join(infile_list)

    options = [proc, out_dir]
    submitCondorJob(proc, executable, options, infile, label="gridpack", submit=(not args.noSub), proxy=args.proxy, isGridpackJob=True)
