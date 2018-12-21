"""Routines for batch processing of cells (v2)."""

import logging

import pandas as pd

from cellpy import prms
from cellpy.utils.batch_tools.batch_exporters import CSVExporter
from cellpy.utils.batch_tools.batch_experiments import CyclingExperiment
from cellpy.utils.batch_tools.batch_plotters import CyclingSummaryPlotter
from cellpy.utils.batch_tools.dumpers import ram_dumper

logger = logging.getLogger(__name__)
logging.captureWarnings(True)


class Batch:
    def __init__(self, *args, **kwargs):
        self.experiment = CyclingExperiment()
        if len(args) > 0:
            self.experiment.journal.name = args[0]

        if len(args) > 1:
            self.experiment.journal.project = args[1]

        for key in kwargs:
            if key == "name":
                self.experiment.journal.name = kwargs[key]
            elif key == "project":
                self.experiment.journal.project = kwargs[key]
            elif key == "batch_col":
                self.experiment.journal.batch_col = kwargs[key]

        self.exporter = CSVExporter()
        self.exporter._assign_dumper(ram_dumper)
        self.exporter.assign(self.experiment)
        self.plotter = CyclingSummaryPlotter()
        self.plotter.assign(self.experiment)
        self._info_df = self.info_file

    def __str__(self):
        return str(self.experiment)

    @property
    def info_file(self):
        return self.experiment.journal.file_name

    @property
    def summaries(self):
        try:
            keys = [df.name for df in self.experiment.memory_dumped["summary_engine"]]
            return pd.concat(self.experiment.memory_dumped["summary_engine"], keys=keys, axis=1)
        except KeyError:
            logging.info("no summary exists")

    @property
    def info_df(self):
        return self.experiment.journal.pages

    @info_df.setter
    def info_df(self, df):
        self.experiment.journal.pages = df

    def create_info_df(self):
        print(self.experiment.journal.name)
        print(self.experiment.journal.project)
        self.experiment.journal.from_db()
        self.experiment.journal.to_file()

    def create_folder_structure(self):
        self.experiment.journal.paginate()

    def save_info_df(self):
        self.experiment.journal.to_file()
        print(self.experiment.journal.pages.head(10))
        print()
        print("saved to:")
        print(self.experiment.journal.file_name)

    def load_and_save_raw(self):
        self.experiment.update()

    def make_summaries(self):
        self.exporter.do()

    def plot_summaries(self):
        self.plotter.do()


def main():
    from pathlib import Path

    # Use these when working on my work PC:
    test_data_path = r"C:\Scripting\MyFiles\development_cellpy\testdata"
    out_data_path = r"C:\Scripting\Processing\Test\out"

    # Use these when working on my MacBook:
    # test_data_path = "/Users/jepe/scripting/cellpy/testdata"
    # out_data_path = "/Users/jepe/cellpy_data"

    test_data_path = Path(test_data_path)
    out_data_path = Path(out_data_path)

    print("---SETTING SOME PRMS---")
    prms.Paths["db_filename"] = "cellpy_db.xlsx"
    prms.Paths["cellpydatadir"] = test_data_path / "hdf5"
    prms.Paths["outdatadir"] = out_data_path
    prms.Paths["rawdatadir"] = test_data_path / "data"
    prms.Paths["db_path"] = test_data_path / "db"
    prms.Paths["filelogdir"] = test_data_path / "log"

    project = "prebens_experiment"
    name = "test"
    batch_col = "b01"

    print("---INITIALISATION OF BATCH---")
    b = init(name, project, batch_col=batch_col)
    b.experiment.export_raw = True
    b.experiment.export_cycles = True
    b.create_info_df()
    b.create_folder_structure()
    b.load_and_save_raw()
    b.make_summaries()
    summaries = b.experiment.memory_dumped

    print("---FINISHED---")


def init(*args, **kwargs):
    """Returns an initialized instance of the Batch class"""
    # set up cellpy logger
    default_log_level = kwargs.pop("default_log_level", None)
    import cellpy.log as log
    log.setup_logging(custom_log_dir=prms.Paths["filelogdir"],
                      default_level=default_log_level)
    return Batch(*args, **kwargs)


if __name__ == "__main__":
    print("---IN BATCH 2 MAIN---")
    main()
