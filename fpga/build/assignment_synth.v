/* Generated by Yosys 0.9+2406 (git sha1 492e2b1, gcc 10.2.1-6 -fPIC -Os) */

(* top =  1  *)
(* src = "/data/data/com.termux/files/home/fpga-examples/assignment/assignment.v:8.1-22.10" *)
module helloworldfpga(x, y, z, w, o);
  (* src = "/data/data/com.termux/files/home/fpga-examples/assignment/assignment.v:15.10-15.13" *)
  wire led;
  (* src = "/data/data/com.termux/files/home/fpga-examples/assignment/assignment.v:13.17-13.18" *)
  output o;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:629.8-629.11" *)
  wire \o_LUT4_O.BA1 ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:630.8-630.11" *)
  wire \o_LUT4_O.BA2 ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:618.8-618.11" *)
  wire \o_LUT4_O.BAB ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:631.8-631.11" *)
  wire \o_LUT4_O.BB1 ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:632.8-632.11" *)
  wire \o_LUT4_O.BB2 ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:616.8-616.11" *)
  wire \o_LUT4_O.BSL ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:607.10-607.12" *)
  wire \o_LUT4_O.I0 ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:608.10-608.12" *)
  wire \o_LUT4_O.I1 ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:609.10-609.12" *)
  wire \o_LUT4_O.I2 ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:610.10-610.12" *)
  wire \o_LUT4_O.I3 ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:606.10-606.11" *)
  wire \o_LUT4_O.O ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:625.8-625.11" *)
  wire \o_LUT4_O.TA1 ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:626.8-626.11" *)
  wire \o_LUT4_O.TA2 ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:617.8-617.11" *)
  wire \o_LUT4_O.TAB ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:627.8-627.11" *)
  wire \o_LUT4_O.TB1 ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:628.8-628.11" *)
  wire \o_LUT4_O.TB2 ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:619.8-619.11" *)
  wire \o_LUT4_O.TBS ;
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:615.8-615.11" *)
  wire \o_LUT4_O.TSL ;
  (* src = "/data/data/com.termux/files/home/fpga-examples/assignment/assignment.v:12.11-12.12" *)
  input w;
  (* src = "/data/data/com.termux/files/home/fpga-examples/assignment/assignment.v:9.11-9.12" *)
  input x;
  (* src = "/data/data/com.termux/files/home/fpga-examples/assignment/assignment.v:10.11-10.12" *)
  input y;
  (* src = "/data/data/com.termux/files/home/fpga-examples/assignment/assignment.v:11.11-11.12" *)
  input z;
  (* module_not_derived = 32'd1 *)
  (* src = "/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:81.9-88.8" *)
  BIDIR_CELL #(
    .DS(1'h0),
    .ESEL(1'h1),
    .FIXHOLD(1'h0),
    .OSEL(1'h1),
    .WPD(1'h0)
  ) _0_ (
    .I_DAT(),
    .I_EN(1'h0),
    .\I_PAD_$inp (),
    .O_DAT(led),
    .O_EN(1'h1),
    .\O_PAD_$out (o)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:43.9-50.8" *)
  BIDIR_CELL #(
    .DS(1'h0),
    .ESEL(1'h1),
    .FIXHOLD(1'h0),
    .OSEL(1'h1),
    .WPD(1'h0)
  ) _1_ (
    .I_DAT(\o_LUT4_O.TBS ),
    .I_EN(1'h1),
    .\I_PAD_$inp (w),
    .O_DAT(),
    .O_EN(1'h0),
    .\O_PAD_$out ()
  );
  (* module_not_derived = 32'd1 *)
  (* src = "/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:43.9-50.8" *)
  BIDIR_CELL #(
    .DS(1'h0),
    .ESEL(1'h1),
    .FIXHOLD(1'h0),
    .OSEL(1'h1),
    .WPD(1'h0)
  ) _2_ (
    .I_DAT(\o_LUT4_O.BSL ),
    .I_EN(1'h1),
    .\I_PAD_$inp (x),
    .O_DAT(),
    .O_EN(1'h0),
    .\O_PAD_$out ()
  );
  (* module_not_derived = 32'd1 *)
  (* src = "/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:43.9-50.8" *)
  BIDIR_CELL #(
    .DS(1'h0),
    .ESEL(1'h1),
    .FIXHOLD(1'h0),
    .OSEL(1'h1),
    .WPD(1'h0)
  ) _3_ (
    .I_DAT(\o_LUT4_O.BAB ),
    .I_EN(1'h1),
    .\I_PAD_$inp (y),
    .O_DAT(),
    .O_EN(1'h0),
    .\O_PAD_$out ()
  );
  (* module_not_derived = 32'd1 *)
  (* src = "/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:43.9-50.8" *)
  BIDIR_CELL #(
    .DS(1'h0),
    .ESEL(1'h1),
    .FIXHOLD(1'h0),
    .OSEL(1'h1),
    .WPD(1'h0)
  ) _4_ (
    .I_DAT(\o_LUT4_O.BA2 ),
    .I_EN(1'h1),
    .\I_PAD_$inp (z),
    .O_DAT(),
    .O_EN(1'h0),
    .\O_PAD_$out ()
  );
  (* module_not_derived = 32'd1 *)
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:40.63-40.132|/data/data/com.termux/files/home/symbiflow/quicklogic-arch-defs/share/techmaps/quicklogic/pp3/techmap/cells_map.v:702.3-718.4" *)
  C_FRAG #(
    .BAS1(1'h1),
    .BAS2(1'h0),
    .BBS1(1'h1),
    .BBS2(1'h0),
    .TAS1(1'h1),
    .TAS2(1'h0),
    .TBS1(1'h1),
    .TBS2(1'h0)
  ) \o_LUT4_O.c_frag  (
    .BA1(1'h0),
    .BA2(\o_LUT4_O.BA2 ),
    .BAB(\o_LUT4_O.BAB ),
    .BB1(\o_LUT4_O.BA2 ),
    .BB2(1'h0),
    .BSL(\o_LUT4_O.BSL ),
    .CZ(led),
    .TA1(1'h0),
    .TA2(\o_LUT4_O.BA2 ),
    .TAB(\o_LUT4_O.BAB ),
    .TB1(\o_LUT4_O.BA2 ),
    .TB2(\o_LUT4_O.BA2 ),
    .TBS(\o_LUT4_O.TBS ),
    .TSL(\o_LUT4_O.BSL )
  );
  assign \o_LUT4_O.TB1  = \o_LUT4_O.BA2 ;
  assign \o_LUT4_O.TB2  = \o_LUT4_O.BA2 ;
  assign \o_LUT4_O.BA1  = 1'h0;
  assign \o_LUT4_O.BB1  = \o_LUT4_O.BA2 ;
  assign \o_LUT4_O.BB2  = 1'h0;
  assign \o_LUT4_O.TAB  = \o_LUT4_O.BAB ;
  assign \o_LUT4_O.TSL  = \o_LUT4_O.BSL ;
  assign \o_LUT4_O.I3  = 1'h0;
  assign \o_LUT4_O.I2  = 1'h0;
  assign \o_LUT4_O.I1  = 1'h0;
  assign \o_LUT4_O.I0  = 1'h0;
  assign \o_LUT4_O.O  = 1'h0;
  assign \o_LUT4_O.TA1  = 1'h0;
  assign \o_LUT4_O.TA2  = \o_LUT4_O.BA2 ;
endmodule