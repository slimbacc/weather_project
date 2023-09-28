"""Imports"""
from pyspark.sql import DataFrame

from weather.common.reader import write_to_parquet
from weather.config.config import app_config
from weather.data.maag_master_agrem.maag_master_agrem_reader import (
    maag_master_agrem_Reader,
)
from weather.data.maag_raty_linked.maag_raty_linked_reader import (
    maag_raty_linked_Reader,
)
from weather.data.maag_repa_rrol_linked.maag_repa_rrol_linked_reader import (
    maag_repa_rrol_linked_Reader,
)
from weather.data.reac_ref_act_type.reac_ref_act_type_reader import (
    reac_ref_act_type_Reader,
)
from weather.data.rtpa_ref_third_party.rtpa_ref_third_party_reader import (
    rtpa_ref_third_party_Reader,
)
from weather.process.functions import rename_common_columns


class ProcessingJobs:
    """init processing job"""
    def __init__(
        self,
        maag_master_agrem_input_path: str,
        reac_ref_act_type_input_path: str,
        maag_repa_rrol_linked_input_path: str,
        maag_raty_linked_input_path: str,
        rtpa_ref_third_party_input_path: str,
        processing_output_path: str,
    ) -> None:

        self.maag_master_agrem_input_path: str = maag_master_agrem_input_path
        self.reac_ref_act_type_input_path: str = reac_ref_act_type_input_path
        self.maag_repa_rrol_linked_input_path: str = (
            maag_repa_rrol_linked_input_path
        )
        self.maag_raty_linked_input_path: str = maag_raty_linked_input_path
        self.rtpa_ref_third_party_input_path: str = (
            rtpa_ref_third_party_input_path
        )
        self.processing_output_path: str = processing_output_path

    def run(self) -> None:
        """processing job"""
        maag_master_agrem_df: DataFrame = (
            self._get_data_from_maag_master_agrem(
                self.maag_master_agrem_input_path
            )
        )
        reac_ref_act_type_df: DataFrame = (
            self._get_data_from_reac_ref_act_type(
                self.reac_ref_act_type_input_path
            )
        )
        maag_repa_rrol_linked_df: DataFrame = (
            self._get_data_from_maag_repa_rrol_linked(
                self.maag_repa_rrol_linked_input_path
            )
        )
        maag_raty_linked_df: DataFrame = (
            self._get_data_from_maag_raty_linked(
                self.maag_raty_linked_input_path
            )
        )
        rtpa_ref_third_party_df: DataFrame = (
            self._get_data_from_rtpa_ref_third_party(
                self.rtpa_ref_third_party_input_path
            )
        )
        final_dataset: DataFrame = self._create_dataset_processing(
            maag_master_agrem_df,
            reac_ref_act_type_df,
            maag_repa_rrol_linked_df,
            maag_raty_linked_df,
            rtpa_ref_third_party_df
            )
        self._write_dataset_to_parquet(
            final_dataset,
            self.processing_output_path
        )

    def _get_data_from_maag_master_agrem(self, path: str) -> DataFrame:
        maag_master_agrem_reader: maag_master_agrem_Reader = (
            maag_master_agrem_Reader(path)
        )
        maag_master_agrem = maag_master_agrem_reader.read()
        return maag_master_agrem

    def _get_data_from_reac_ref_act_type(self, path: str) -> DataFrame:
        reac_ref_act_type_reader: reac_ref_act_type_Reader = (
            reac_ref_act_type_Reader(path)
        )
        reac_ref_act_type = reac_ref_act_type_reader.read()
        return reac_ref_act_type

    def _get_data_from_maag_repa_rrol_linked(self, path: str) -> DataFrame:
        maag_repa_rrol_linked_reader: maag_repa_rrol_linked_Reader = (
            maag_repa_rrol_linked_Reader(path)
        )
        maag_repa_rrol_linked = maag_repa_rrol_linked_reader.read()
        return maag_repa_rrol_linked

    def _get_data_from_maag_raty_linked(self, path: str) -> DataFrame:
        maag_raty_linked_reader: maag_raty_linked_Reader = (
            maag_raty_linked_Reader(path)
        )
        maag_raty_linked = maag_raty_linked_reader.read()
        return maag_raty_linked

    def _get_data_from_rtpa_ref_third_party(self, path: str) -> DataFrame:
        rtpa_ref_third_party_reader: rtpa_ref_third_party_Reader = (
            rtpa_ref_third_party_Reader(path)
        )
        rtpa_ref_third_party = rtpa_ref_third_party_reader.read()
        return rtpa_ref_third_party

    def _create_dataset_processing(
            self,
            maag_master_agrem_df: DataFrame,
            reac_ref_act_type_df: DataFrame,
            maag_repa_rrol_linked_df: DataFrame,
            maag_raty_linked_df: DataFrame,
            rtpa_ref_third_party_df: DataFrame) -> DataFrame:
        
        return

    def _write_dataset_to_parquet(
            self,
            df: DataFrame,
            output_path: str) -> None:
        write_to_parquet(df, output_path)


def run_job() -> None:
    """run the processing job"""
    file_path_maag_master_agrem = app_config.file_path_maag_master_agrem
    file_path_reac_ref_act_type = app_config.file_path_reac_ref_act_type
    file_path_maag_repa_rrol_linked = (
        app_config.file_path_maag_repa_rrol_linked
    )
    file_path_maag_raty_linked = app_config.file_path_maag_raty_linked
    file_path_rtpa_ref_third_party = app_config.file_path_rtpa_ref_third_party
    output_file_path_processing = app_config.output_file_path_processing

    maag_master_agrem_path: str = file_path_maag_master_agrem
    reac_ref_act_type_path: str = file_path_reac_ref_act_type
    maag_repa_rrol_linked_path: str = file_path_maag_repa_rrol_linked
    maag_raty_linked_path: str = file_path_maag_raty_linked
    rtpa_ref_third_party_path: str = file_path_rtpa_ref_third_party
    processing_output_path: str = output_file_path_processing

    job: ProcessingJobs = ProcessingJobs(
        maag_master_agrem_path,
        reac_ref_act_type_path,
        maag_repa_rrol_linked_path,
        maag_raty_linked_path,
        rtpa_ref_third_party_path,
        processing_output_path
    )
    job.run()
