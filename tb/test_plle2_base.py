import test_base

import shutil
import os

from avocado import Test


class Plle2BaseTest(Test, test_base.Mixin):
    """
    This class tests the plle2_base.v module.
    """

    def setUp(self):
        """
        This function is needed in every test class.
        """
        # main directory of the project
        self.project_dir = os.path.dirname(self.basedir)

        # change to workdir so simulation process find the source files
        os.chdir(self.workdir)

    def generic_plle2_base_test(self,
                                wait_interval=500,
                                bandwidth=r'\"OPTIMIZED\"',

                                clkfbout_mult=5,
                                clkfbout_phase=0.000,

                                clkin1_period=5.000,

                                clkout0_divide=1,
                                clkout1_divide=1,
                                clkout2_divide=1,
                                clkout3_divide=1,
                                clkout4_divide=1,
                                clkout5_divide=1,

                                clkout0_duty_cycle=0.500,
                                clkout1_duty_cycle=0.500,
                                clkout2_duty_cycle=0.500,
                                clkout3_duty_cycle=0.500,
                                clkout4_duty_cycle=0.500,
                                clkout5_duty_cycle=0.500,

                                clkout0_phase=0.000,
                                clkout1_phase=0.000,
                                clkout2_phase=0.000,
                                clkout3_phase=0.000,
                                clkout4_phase=0.000,
                                clkout5_phase=0.000,

                                divclk_divide=1,

                                ref_jitter1=0.010,
                                startup_wait=r'\"FALSE\"'):
        """test plle2 base"""

        test_files = ["plle2_base_tb.v"]
        src_files = ["phase_shift.v",
                     "plle2_base.v",
                     "freq_gen.v",
                     "period_check.v",
                     "period_count.v",
                     "dyn_reconf.v",
                     "pll.v",
                     "phase_shift_check.v",
                     "duty_cycle_check.v"]
        # copy source files so we know that all required files are there
        self.copy_sources(test_files, src_files)

        verilog_files = test_files + src_files

        sim_res = self.simulate(verilog_files,
                                """
                                -DWAIT_INTERVAL={} \

                                -DBANDWIDTH={} \

                                -DCLKFBOUT_MULT={} \
                                -DCLKFBOUT_PHASE={} \

                                -DCLKIN1_PERIOD={} \

                                -DCLKOUT0_DIVIDE={} \
                                -DCLKOUT1_DIVIDE={} \
                                -DCLKOUT2_DIVIDE={} \
                                -DCLKOUT3_DIVIDE={} \
                                -DCLKOUT4_DIVIDE={} \
                                -DCLKOUT5_DIVIDE={} \

                                -DCLKOUT0_DUTY_CYCLE={} \
                                -DCLKOUT1_DUTY_CYCLE={} \
                                -DCLKOUT2_DUTY_CYCLE={} \
                                -DCLKOUT3_DUTY_CYCLE={} \
                                -DCLKOUT4_DUTY_CYCLE={} \
                                -DCLKOUT5_DUTY_CYCLE={} \

                                -DCLKOUT0_PHASE={} \
                                -DCLKOUT1_PHASE={} \
                                -DCLKOUT2_PHASE={} \
                                -DCLKOUT3_PHASE={} \
                                -DCLKOUT4_PHASE={} \
                                -DCLKOUT5_PHASE={} \

                                -DDIVCLK_DIVIDE={} \

                                -DREF_JITTER1={} \
                                -DSTARTUP_WAIT={}"""
                                .format(
                                    wait_interval,

                                    bandwidth,

                                    clkfbout_mult,
                                    clkfbout_phase,

                                    clkin1_period,

                                    clkout0_divide,
                                    clkout1_divide,
                                    clkout2_divide,
                                    clkout3_divide,
                                    clkout4_divide,
                                    clkout5_divide,

                                    clkout0_duty_cycle,
                                    clkout1_duty_cycle,
                                    clkout2_duty_cycle,
                                    clkout3_duty_cycle,
                                    clkout4_duty_cycle,
                                    clkout5_duty_cycle,

                                    clkout0_phase,
                                    clkout1_phase,
                                    clkout2_phase,
                                    clkout3_phase,
                                    clkout4_phase,
                                    clkout5_phase,

                                    divclk_divide,

                                    ref_jitter1,

                                    startup_wait)
                                .replace("\n", "").replace("\t", ""))
        sim_output = sim_res.stdout_text

        # save vcd for analysis
        shutil.copy("plle2_base_tb.vcd", self.outputdir)

        self.check_test_bench_output(sim_output, 24)

    def test_plle2_base_default(self):
        """
        :avocado: tags:quick,verilog
        """

        self.generic_plle2_base_test()

    def test_plle2_base_clkfbout_clkin1_divclk(self):
        """
        :avocado: tags:quick,verilog
        """

        self.generic_plle2_base_test(
            clkfbout_mult=64, clkin1_period=20.000, divclk_divide=4)

    def test_plle2_base_clkout0(self):
        """
        :avocado: tags:quick,verilog
        """

        self.generic_plle2_base_test(
            clkout0_divide=5, clkout0_duty_cycle=0.100)

    def test_plle2_base_clkout5(self):
        """
        :avocado: tags:quick,verilog
        """

        self.generic_plle2_base_test(
            clkout5_divide=10, clkout5_duty_cycle=0.85)

    def test_plle2_base_clkout1_clkout2_divclk_clkfb(self):
        """
        :avocado: tags:quick,verilog
        """

        self.generic_plle2_base_test(clkout1_divide=3,
                                     clkout1_duty_cycle=0.450,
                                     clkout2_divide=8,
                                     clkout2_duty_cycle=0.333,
                                     divclk_divide=2,
                                     clkfbout_mult=8)

    def test_plle2_base_phase(self):
        """
        :avocado: tags:quick, verilog
        """

        self.generic_plle2_base_test(clkfbout_phase=90,
                                     clkout0_phase=22.5,
                                     clkout1_phase=45,
                                     clkout2_phase=90,
                                     clkout3_phase=180,
                                     clkout4_phase=270,
                                     clkout5_phase=-60)

    def test_plle2_base_showcase(self):
        """
        :avocado: tags:verilog
        """

        self.generic_plle2_base_test(clkout0_divide=2,
                                     clkout1_duty_cycle=0.1,
                                     clkout2_duty_cycle=0.9,
                                     clkout3_phase=180,
                                     clkout4_phase=-90,
                                     clkout5_divide=4,
                                     clkout5_duty_cycle=0.3,
                                     clkfbout_mult=4)
