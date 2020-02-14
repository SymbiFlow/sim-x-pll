/*
 * dyn_reconf.v: Handles the reconfiguration process of the pll.
 * author: Till Mahlburg
 * year: 2020
 * organization: Universität Leipzig
 * license: ISC
 *
 */

`timescale 1 ns / 1 ps

module dyn_reconf (
	input RST,
	input PWRDWN,

	input [6:0] DADDR,
	input DCLK,
	input DEN,
	input DWE,
	input [15:0] DI,

	output reg [15:0] DO,
	output reg DRDY);

	/* registers for dynamic output reconfiguration */
	reg [15:0] ClkReg1[0:6];
	reg [15:0] ClkReg1_FB;

	reg [15:0] ClkReg2[0:6];
	reg [15:0] ClkReg2_FB;

	reg [15:0] DivReg;

	reg [15:0] LockReg[1:3];

	reg [15:0] FiltReg[1:2];

	reg [15:0] PowerReg;


	always @(posedge DCLK or posedge RST or posedge PWRDWN) begin
		if (PWRDWN) begin
			DRDY <= 1'bx;
			DO <= 16'hXXXX;
		end else if (RST) begin
			DRDY <= 1'b0;
			DO <= 16'h0000;
		end else if (DEN) begin
			DRDY <= 1'b0;
			/* Write */
			if (DWE) begin
				case (DADDR)
					7'h06 : ClkReg1_5 <= DI;
					7'h07 : ClkReg2_5 <= DI;
					7'h08 : ClkReg1_0 <= DI;
					7'h09 : ClkReg2_0 <= DI;
					7'h0A : ClkReg1_1 <= DI;
					7'h0B : ClkReg2_1 <= DI;
					7'h0C : ClkReg1_2 <= DI;
					7'h0D : ClkReg2_2 <= DI;
					7'h0E : ClkReg1_3 <= DI;
					7'h0F : ClkReg2_3 <= DI;
					7'h10 : ClkReg1_4 <= DI;
					7'h11 : ClkReg2_4 <= DI;
					7'h12 : ClkReg1_6 <= DI;
					7'h13 : ClkReg2_6 <= DI;
					7'h14 : ClkReg1_FB <= DI;
					7'h15 : ClkReg2_FB <= DI;
					7'h16 : DivReg <= DI;
					7'h18 : LockReg1 <= DI;
					7'h19 : LockReg2 <= DI;
					7'h1A : LockReg3 <= DI;
					7'h28 : PowerReg <= DI;
					7'h4E : FiltReg1 <= DI;
					7'h4F : FiltReg2 <= DI;
					default : $display("default"); //TODO;
				endcase
			/* Read */
			end else begin
				case (DADDR)
					7'h06 : DO <= ClkReg1_5;
					7'h07 : DO <= ClkReg2_5;
					7'h08 : DO <= ClkReg1_0;
					7'h09 : DO <= ClkReg2_0;
					7'h0A : DO <= ClkReg1_1;
					7'h0B : DO <= ClkReg2_1;
					7'h0C : DO <= ClkReg1_2;
					7'h0D : DO <= ClkReg2_2;
					7'h0E : DO <= ClkReg1_3;
					7'h0F : DO <= ClkReg2_3;
					7'h10 : DO <= ClkReg1_4;
					7'h11 : DO <= ClkReg2_4;
					7'h12 : DO <= ClkReg1_6;
					7'h13 : DO <= ClkReg2_6;
					7'h14 : DO <= ClkReg1_FB;
					7'h15 : DO <= ClkReg2_FB;
					7'h16 : DO <= DivReg;
					7'h18 : DO <= LockReg1;
					7'h19 : DO <= LockReg2;
					7'h1A : DO <= LockReg3;
					7'h28 : DO <= PowerReg;
					7'h4E : DO <= FiltReg1;
					7'h4F : DO <= FiltReg2;
					default : $display("default"); //TODO;
				endcase
			end
		end else begin
			DRDY <= 1'b1;
		end
	end
endmodule
