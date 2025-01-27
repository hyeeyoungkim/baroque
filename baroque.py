import argparse

from baroque import defaults
from baroque.baroque_project import BaroqueProject
from baroque.config import get_config_setting
from baroque.mets_validation import MetsValidator
from baroque.report_generation import generate_reports
from baroque.structure_validation import StructureValidator
from baroque.wav_bext_chunk_validation import WavBextChunkValidator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Path to source directory")
    parser.add_argument("export", help="Path to metadata export")
    parser.add_argument("-d", "--destination", help="Path to destination for reports")
    parser.add_argument("-s", "--structure", action="store_true", help="Validate directory and file structure")
    parser.add_argument("-m", "--mets", action="store_true", help="Validate METS")
    parser.add_argument("-w", "--wav", action="store_true", help="Validate WAV BEXT chunks")
    args = parser.parse_args()

    if args.destination:
        destination = args.destination
    else:
        destination = get_config_setting("destination", default=defaults.REPORTS_DIR)

    project = BaroqueProject(args.source, destination, args.export)
    if args.structure:
        StructureValidator(project).validate()
    if args.mets:
        MetsValidator(project).validate()
    if args.wav:
        WavBextChunkValidator(project).validate()

    generate_reports(project)


if __name__ == "__main__":
    print("SYSTEM ACTIVITY: baroque starting")
    main()
    print("SYSTEM ACTIVITY: baroque finished")
