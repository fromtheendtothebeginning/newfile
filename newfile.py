from manimlib import *

# manimgl D:\start\newfile\newfile.py happy -o --hd -c WHITE

x = 0.15 * 1.414
u = 1 / (82 ** (1 / 2))


class happy(Scene):
    def construct(self):
        # 基础元件部件
        cp_s = Line(start=np.array([0.1, 0, 0]),
                    end=np.array([0.5, 0, 0]))
        o1p_s = Line(start=np.array([0.06, 0.08, 0]),
                     end=np.array([0.3, 0.4, 0]))
        o2p_s = Line(start=np.array([0.06, -0.08, 0]),
                     end=np.array([0.3, -0.4, 0]))
        lcp_s = Line(start=np.array([0, 0.1, 0]),
                     end=np.array([0, 0.5, 0]))
        lo1p_s = Line(start=np.array([-0.08, 0.06, 0]),
                      end=np.array([-0.4, 0.3, 0]))
        lo2p_s = Line(start=np.array([0.08, 0.06, 0]),
                      end=np.array([0.4, 0.3, 0]))
        dc_1 = Line(start=np.array([-0.1, -0.1, 0]),
                    end=np.array([-0.1, 0.1, 0]))
        dc_2 = Line(start=np.array([0.1, -0.3, 0]),
                    end=np.array([0.1, 0.3, 0]))
        lt_1 = Circle().scale(0.3)
        lt_21 = Line(start=np.array([x, x, 0]),
                     end=np.array([-x, -x, 0]))
        lt_22 = Line(start=np.array([-x, x, 0]),
                     end=np.array([x, -x, 0]))
        dct_1 = Rectangle(height=0.5, width=0.7 * 1.3)
        dct_21 = Line(start=np.array([0.45, 0.25, 0]),
                      end=np.array([0.225, -0.25, 0]))
        dct_22 = Line(start=np.array([0.225, 0.25, 0]),
                      end=np.array([0, -0.25, 0]))
        dct_23 = Line(start=np.array([0, 0.25, 0]),
                      end=np.array([-0.225, -0.25, 0]))
        dct_24 = Line(start=np.array([-0.225, 0.25, 0]),
                      end=np.array([-0.45, -0.25, 0]))

        # 基础元件
        o = Circle().scale(0.1)
        cp = VGroup(o, cp_s).set_color(BLACK)
        o1p = VGroup(o, o1p_s).set_color(BLACK)
        o2p = VGroup(o, o2p_s).set_color(BLACK)
        lcp = VGroup(o, lcp_s).set_color(BLACK)
        lo1p = VGroup(o, lo1p_s).set_color(BLACK)
        lo2p = VGroup(o, lo2p_s).set_color(BLACK)
        Dc = VGroup(dc_1, dc_2).set_color(BLACK)
        light0 = VGroup(lt_1, lt_21, lt_22) \
            .set_color(BLACK).scale(0.75)
        Dz = Rectangle(height=0.25, width=0.45) \
            .set_color(BLACK)
        Dct = VGroup(dct_1, dct_21, dct_22, dct_23, dct_24) \
            .set_color(BLACK)

        # 控制电路元件
        dDc_1 = Dc.copy().shift(np.array([0, -2, 0]))
        dDct_1 = Dct.copy().shift(np.array([1, 2, 0])) \
            .rotate(PI / 2)
        dL3 = Line(start=np.array([2, 2, 0]),
                   end=np.array([1.25, 2, 0])) \
            .set_color(BLACK)
        dL2 = Line(start=np.array([2, -2, 0]),
                   end=np.array([2, 2, 0])) \
            .set_color(BLACK)
        dL1 = Line(start=np.array([0.125, -2, 0]),
                   end=np.array([2, -2, 0])) \
            .set_color(BLACK)
        dL4 = Line(start=np.array([0.75, 2, 0]),
                   end=np.array([0, 2, 0])) \
            .set_color(BLACK)
        do1p_1 = o1p.copy().shift(np.array([-0.3, 2, 0])) \
            .rotate(PI, np.array([0, 2, 0]))
        do2p_1 = o2p.copy().shift(np.array([-0.3, 2, 0])) \
            .rotate(PI, np.array([0, 2, 0])) \
            .shift(np.array([0.5, 0, 0]))
        dL5 = Line(start=np.array([-0.4, 2.4, 0]),
                   end=np.array([-1.7, 2.4, 0])) \
            .set_color(BLACK)
        dDz_1 = Dz.copy().shift(np.array([-1, -2, 0]))
        dL6 = Line(start=np.array([-0.1, -2, 0]),
                   end=np.array([-0.75, -2, 0])) \
            .set_color(BLACK)
        dL7 = Line(start=np.array([-1.25, -2, 0]),
                   end=np.array([-3, -2, 0])) \
            .set_color(BLACK)
        dL8 = Line(start=np.array([-3, -2, 0]),
                   end=np.array([-3, 2, 0])) \
            .set_color(BLACK)
        dL9 = Line(start=np.array([-3, 2, 0]),
                   end=np.array([-2.1, 2, 0])) \
            .set_color(BLACK)
        do1p_2 = o2p.copy().shift(np.array([-2, 2, 0]))
        do2p_2 = o1p.copy().shift(np.array([-2, 2, 0])) \
            .shift(np.array([0.5, 0, 0]))
        dL10 = Line(start=np.array([-1.7, 1.6, 0]),
                    end=np.array([-0.4, 1.6, 0])) \
            .set_color(BLACK)
        dLt_o = light0.copy().set_color(BLACK) \
            .shift(np.array([1.5, 2, 0]))
        dLt_c = light0.copy().set_color(YELLOW_E) \
            .shift(np.array([1.5, 2, 0]))

        # 控制电路
        # u上d下,L左R右,l有灯
        # 无l有电磁铁,c灯亮,o灯灭
        D_R_lu_o = VGroup(dDc_1, dL1, dL2, dL3,
                          dLt_o, dL4, do1p_1, dL5)
        D_R_lu_c = VGroup(dDc_1, dL1, dL2, dL3,
                          dLt_c, dL4, do1p_1, dL5)
        D_R_ld_o = VGroup(dDc_1, dL1, dL2, dL3,
                          dLt_o, dL4, do2p_1, dL5)
        D_R_ld_c = VGroup(dDc_1, dL1, dL2, dL3,
                          dLt_c, dL4, do2p_1, dL5)
        D_R_u = VGroup(dDc_1, dL1, dL2, dL3,
                       dDct_1, dL4, do1p_1, dL5) \
            .shift(np.array([0.5, 0, 0]))
        D_L_d = VGroup(dL6, dDz_1, dL7, dL8,
                       dL9, do1p_2, dL10) \
            .shift(np.array([0.5, 0, 0]))
        D_R_d = VGroup(dDc_1, dL1, dL2, dL3,
                       dDct_1, dL4, do2p_1, dL5)
        D_L_u = VGroup(dL6, dDz_1, dL7, dL8,
                       dL9, do2p_2, dL10)

        # 电磁继电器元件
        dcj_dc = Dc.copy().shift(np.array([-3, -2, 0]))
        dcj_l11 = Line(start=np.array([-3.1, -2, 0]),
                       end=np.array([-4, -2, 0]))
        dcj_l12 = Line(start=np.array([-4, -2, 0]),
                       end=np.array([-4, 1, 0]))
        dcj_l13 = Line(start=np.array([-4, 1, 0]),
                       end=np.array([-3.25, 1, 0]))
        dcj_dz = Dz.copy().shift(np.array([-3, 1, 0]))
        dcj_l14 = Line(start=np.array([-2.75, 1, 0]),
                       end=np.array([-1.3, 1, 0]))
        dcj_l21 = Line(start=np.array([-2.9, -2, 0]),
                       end=([-2.1, -2, 0]))
        dcj_o = o1p.copy().shift(np.array([-2, -2, 0]))
        dcj_c = cp.copy().shift(np.array([-2, -2, 0]))
        dcj_l22 = Line(start=np.array([-1.5, -2, 0]),
                       end=np.array([0, -2, 0]))
        dcj_l23 = Line(start=np.array([0, -2, 0]),
                       end=np.array([0, 1, 0]))
        dcj_l24 = Line(start=np.array([0, 1, 0]),
                       end=np.array([-0.7, 1, 0]))
        dcj_dct = Dct.copy() \
            .shift(np.array([-1, 1, 0])) \
            .rotate(PI / 2)
        dcj_l25 = Line(start=np.array([-2.75, 2.75, 0]),
                       end=np.array([-2.25, 2.75, 0]))
        dcj_l26 = Line(start=np.array([-2.5, 2.75, 0]),
                       end=np.array([-2.5, 2.1, 0]))
        dcj_uo = o.copy().shift(np.array([-2.5, 2, 0]))
        dcj_l27_o = Line(start=np.array([-2.4, 2, 0]),
                         end=np.array([-1.25, 2, 0]))
        dcj_l27_c = Line(start=np.array([-2.4, 2, 0]),
                         end=np.array([-2.4 + 11.25 * u, 2 - 1.25 * u, 0]))
        dcj_udz_o = Dz.copy().shift(np.array([-1, 2, 0]))
        dcj_udz_c = Dz.copy().shift(np.array([-2.4 + 13.5 * u, 2 - 1.5 * u, 0]))
        dcj_udz_c.rotate(-np.arccos(9 * u))
        dcj_l28_o = Line(start=np.array([-0.75, 2, 0]),
                         end=np.array([1.75, 2, 0]))
        dcj_l28_c = Line(start=np.array([-2.4 + 1.75 * 9 * u, 2 - 1.75 * u, 0]),
                         end=np.array([-2.4 + 4.2 * 9 * u, 2 - 4.2 * u, 0]))
        dcj_u2dz_o = Dz.copy().shift(np.array([2, 2, 0]))
        dcj_u2dz_c = Dz.copy().shift(np.array([2, 1.5, 0])) \
            .rotate(-np.arccos(9 * u))
        dcju_dc = Dc.copy().shift(np.array([2, -2, 0]))
        dcju_l11 = Line(start=np.array([1.9, -2, 0]),
                        end=np.array([1, -2, 0]))
        dcju_l12_o = Line(start=np.array([1, -2, 0]),
                          end=np.array([1, 2, 0]))
        dcju_l12_c = Line(start=np.array([1, -2, 0]),
                          end=np.array([1, 1.6, 0]))
        dcju_l21 = Line(start=np.array([2.1, -2, 0]),
                        end=np.array([2.765, -2, 0]))
        dcju_o = light0.copy().shift(np.array([3, -2, 0]))
        dcju_c = light0.copy().shift(np.array([3, -2, 0])) \
            .set_color(YELLOW_E)
        dcju_l22 = Line(start=np.array([3.225, -2, 0]),
                        end=np.array([4, -2, 0]))
        dcju_l23 = Line(start=np.array([4, -2, 0]),
                        end=np.array([4, 1, 0]))
        dcju_l24 = Line(start=np.array([4, 1, 0]),
                        end=np.array([2, 1, 0]))
        dcju_l25 = Line(start=np.array([2, 1, 0]),
                        end=np.array([2, 1.38, 0]))

        # 电磁继电器电路
        # L左,R右 U是工作电路,
        # 需要L,R,UL,UR各一个
        # o开关断开,c闭合
        DcjL = VGroup(dcj_dc, dcj_l11, dcj_l12,
                      dcj_l13, dcj_dz, dcj_l14) \
            .set_color(BLACK)
        DcjR_o = VGroup(dcj_l21, dcj_o, dcj_l22,
                        dcj_l23, dcj_l24, dcj_dct,
                        dcj_l25, dcj_uo, dcj_l26,
                        dcj_l27_o, dcj_udz_o, dcj_l28_o,
                        dcj_u2dz_o).set_color(BLACK)
        DcjR_c = VGroup(dcj_l21, dcj_c, dcj_l22,
                        dcj_l23, dcj_l24, dcj_dct,
                        dcj_l25, dcj_uo, dcj_l26,
                        dcj_l27_c, dcj_udz_c, dcj_l28_c,
                        dcj_u2dz_c).set_color(BLACK)
        DcjUL_o = VGroup(dcju_dc, dcju_l11, dcju_l12_o) \
            .set_color(BLACK)
        DcjUL_c = VGroup(dcju_dc, dcju_l11, dcju_l12_c) \
            .set_color(BLACK)
        DcjUR_o = VGroup(dcju_l21, dcju_o, dcju_l22,
                         dcju_l23, dcju_l24, dcju_l25) \
            .set_color(BLACK)
        DcjUR_c = VGroup(dcju_l21, dcju_c, dcju_l22,
                         dcju_l23, dcju_l24, dcju_l25)

        # 单向开关电路元件
        old_dc = Dc.copy().shift(np.array([0, -2, 0]))
        old_l11 = Line(start=np.array([-0.1, -2, 0]),
                       end=np.array([-2, -2, 0]))
        old_l12 = Line(start=np.array([-2, -2, 0]),
                       end=np.array([-2, -0.225, 0]))
        old_dz1 = Dz.copy() \
            .shift(np.array([-2, 0, 0])).rotate(PI / 2)
        old_l13 = Line(start=np.array([-2, 0.225, 0]),
                       end=np.array([-2, 2, 0]))
        old_l14 = Line(start=np.array([-2, 2, 0]),
                       end=np.array([3, 2, 0]))
        old_l15 = Line(start=np.array([3, 2, 0]),
                       end=np.array([3, 0.225, 0]))
        old_dz2 = old_dz1.copy().shift(np.array([5, 0, 0]))
        old_l16 = Line(start=np.array([3, -0.225, 0]),
                       end=np.array([3, -2, 0]))
        old_l17 = Line(start=np.array([3, -2, 0]),
                       end=np.array([1.225, -2, 0]))
        old_dz3 = Dz.copy().shift(np.array([1, -2, 0]))
        old_l18 = Line(start=np.array([0.775, -2, 0]),
                       end=np.array([0.1, -2, 0]))
        old_l21 = Line(start=np.array([-1, -2, 0]),
                       end=np.array([-1, -1.1, 0]))
        old_l22 = Line(start=np.array([-1, -0.5, 0]),
                       end=np.array([-1, 0.5, 0]))
        old_l23 = Line(start=np.array([-1, 0.5, 0]),
                       end=np.array([2, 0.5, 0]))
        old_l24 = Line(start=np.array([2, 0.5, 0]),
                       end=np.array([2, -0.5, 0]))
        old_l25 = Line(start=np.array([2, -1.1, 0]),
                       end=np.array([2, -2, 0]))
        old_l26 = Line(start=np.array([0.5, 0.5, 0]),
                       end=np.array([0.5, 1, 0]))
        old_l27 = Line(start=np.array([0.5, 1.5, 0]),
                       end=np.array([0.5, 2, 0]))
        old_lt_o = light0.set_color(BLACK) \
            .shift(np.array([0.5, 1.25, 0]))
        old_lt_c = old_lt_o.copy().set_color(YELLOW_E)
        old_op1 = lo1p.copy() \
            .shift(np.array([-1, -1, 0]))
        old_cp1 = lcp.copy() \
            .shift(np.array([-1, -1, 0]))
        old_op2 = lo1p.copy() \
            .shift(np.array([2, -1, 0]))
        old_cp2 = lcp.copy() \
            .shift(np.array([2, -1, 0]))
        sold_Lt_o = old_lt_o.copy()

        # 单向开关电路元件
        # in里 out外
        # 需要in out各一个
        # uv,u是左开关状态,v是右开关
        OD_in = VGroup(old_l21, old_l22, old_l23,
                       old_l24, old_l25, old_l26, old_l27) \
            .set_color(BLACK)
        OD_in00 = VGroup(old_l21, old_op1, old_l22, old_l23,
                         old_l24, old_l25, old_op2, old_l26,
                         old_lt_o, old_l27)
        OD_in01 = VGroup(old_l21, old_op1, old_l22, old_l23,
                         old_l24, old_l25, old_cp2, old_l26,
                         old_lt_c, old_l27)
        OD_in10 = VGroup(old_l21, old_cp1, old_l22, old_l23,
                         old_l24, old_l25, old_op2, old_l26,
                         old_lt_c, old_l27)
        OD_in11 = VGroup(old_l21, old_cp1, old_l22, old_l23,
                         old_l24, old_l25, old_cp2, old_l26,
                         sold_Lt_o, old_l27)
        OD_out = VGroup(old_dc, old_l11, old_l12,
                        old_dz1, old_l13, old_l14,
                        old_l15, old_dz2, old_l16,
                        old_l17, old_dz3, old_l18) \
            .set_color(BLACK)

        # 红线描述元件
        old_rxy_l1 = Line(start=np.array([-0.13, -2, 0]),
                          end=np.array([-2, -2, 0]))
        old_rxy_l2 = Line(start=np.array([-2, -2, 0]),
                          end=np.array([-2, -0.27, 0]))
        old_rxy_l3 = Line(start=np.array([-2, 0.27, 0]),
                          end=np.array([-2, 2, 0]))
        old_rxy_l4 = Line(start=np.array([-2, 2, 0]),
                          end=np.array([3, 2, 0]))
        old_rxy_l5 = Line(start=np.array([3, 2, 0]),
                          end=np.array([3, 0.27, 0]))
        old_rxy_l6 = Line(start=np.array([3, -0.27, 0]),
                          end=np.array([3, -2, 0]))
        old_rxy_l7 = Line(start=np.array([3, -2, 0]),
                          end=np.array([1.27, -2, 0]))
        old_rxy_l8 = Line(start=np.array([0.73, -2, 0]),
                          end=np.array([0.13, -2, 0]))
        old_r1y_l1 = Line(start=np.array([-1, -2, 0]),
                          end=np.array([-1, 0.5, 0]))
        old_r10_l2 = Line(start=np.array([-1, 0.5, 0]),
                          end=np.array([0.5, 0.5, 0]))
        old_r11_l2 = Line(start=np.array([-1, 0.5, 0]),
                          end=np.array([2, 0.5, 0]))
        old_rxy_ll1 = Line(start=np.array([0.5, 0.5, 0]),
                           end=np.array([0.5, 1, 0]))
        old_rxy_ll2 = Line(start=np.array([0.5, 1.5, 0]),
                           end=np.array([0.5, 2, 0]))
        old_rx1_l3 = Line(start=np.array([0.5, 0.5, 0]),
                          end=np.array([2, 0.5, 0]))
        old_rx1_l4 = Line(start=np.array([2, 0.5, 0]),
                          end=np.array([2, -2, 0]))
        old_r11_start = Line(start=np.array([-0.13, -2, 0]),
                             end=np.array([-1, -2, 0]))
        old_r11_end1 = Line(start=np.array([2, -2, 0]),
                            end=np.array([1.27, -2, 0]))
        old_r11_end2 = Line(start=np.array([0.73, -2, 0]),
                            end=np.array([0.13, -2, 0]))

        # 红线描述
        # uv对应原电路uv
        OD_r00 = VGroup(old_rxy_l1, old_rxy_l2, old_rxy_l3,
                        old_rxy_l4, old_rxy_l5, old_rxy_l6, old_rxy_l7,
                        old_rxy_l8) \
            .set_color(RED_D)
        OD_r01 = VGroup(old_rxy_l1, old_rxy_l2, old_rxy_l3,
                        old_rxy_l4, old_rxy_l5, old_rxy_l6,
                        old_rxy_l7, old_rxy_l8,
                        old_rxy_ll1, old_rxy_ll2,
                        old_rx1_l3, old_rx1_l4) \
            .set_color(RED_D)
        OD_r10 = VGroup(old_rxy_l1, old_rxy_l2, old_rxy_l3,
                        old_rxy_l4, old_rxy_l5, old_rxy_l6,
                        old_rxy_l7, old_rxy_l8,
                        old_r1y_l1, old_r10_l2,
                        old_rxy_ll1, old_rxy_ll2) \
            .set_color(RED_D)
        OD_r11 = VGroup(old_r11_start, old_r1y_l1,
                        old_r11_l2, old_rx1_l4,
                        old_r11_end1, old_r11_end2) \
            .set_color(RED_D)

        # 电磁继电器简化元件部件
        DcjU_sq = Rectangle(height=0.7, width=0.45)
        DcjU_o = o.copy().shift(np.array([0, 0.35, 0])) \
            .set_fill(BLACK, opacity=1)
        DcjU_o1p = Line(start=np.array([0, 0.35, 0]),
                        end=np.array([-0.3, 0.75, 0]))
        DcjU_o2p = Line(start=np.array([0, 0.35, 0]),
                        end=np.array([0.3, 0.75, 0]))
        DcjU_cp = Line(start=np.array([0, 0.35, 0]),
                       end=np.array([0, 1.35, 0]))

        # 电磁继电器元件
        so1d = VGroup(DcjU_sq, DcjU_o, DcjU_o1p) \
            .set_color(BLACK)
        so2d = VGroup(DcjU_sq, DcjU_o, DcjU_o2p) \
            .set_color(BLACK)
        scd = VGroup(DcjU_sq, DcjU_o, DcjU_cp) \
            .set_color(BLACK)

        # 正片
        t0 = Text(
            "The only real valuable thing is intuition. \nThe intellect has little to do \non the road to discovery.") \
            .shift(UP) \
            .set_color(GREY_E) \
            .scale(0.5)
        t0_s = Text("--Nikola Tesla") \
            .next_to(t0, DOWN + RIGHT) \
            .set_color(GREY_E).scale(0.5)
        t0ss1 = Text("真正有价值的是直觉",
                     font="思源黑体") \
            .shift(np.array([0, -1, 0])) \
            .set_color(GREY_E) \
            .scale(0.5)
        t0ss2 = Text("在探索的道路上智力无甚用处",
                     font="思源黑体") \
            .next_to(t0ss1, DOWN).set_color(GREY_E) \
            .scale(0.5)
        t0s_s = Text("--尼古拉 特斯拉",
                     font="思源黑体") \
            .next_to(t0ss2, DOWN + RIGHT) \
            .set_color(GREY_E).scale(0.5)
        t0ss = VGroup(t0ss1, t0ss2)
        t1 = Text("这是一个有两个单闸开关构成的",
                  font="思源黑体", ) \
            .shift(np.array([0, -3.5, 0])) \
            .set_color(GREY_D) \
            .scale(0.5)
        t1s = Text("  开关每一次状态的改变\n都会造成电器状态的改变",
                   font="思源黑体", ) \
            .set_color(GREY_D) \
            .shift(np.array([0, -3.5, 0])) \
            .scale(0.5)
        cOD_r00 = OD_r00.copy()
        cOD_r01 = OD_r01.copy()
        cOD_r11 = OD_r11.copy()
        cOD_r10 = OD_r10.copy()
        t2 = Text("当然还有更好的选择",
                  font="思源黑体", ) \
            .set_color(GREY_D) \
            .shift(np.array([0, -3.5, 0])) \
            .scale(0.5)
        cDR = D_R_lu_o.copy()
        cDL = D_L_d.copy()
        C = VGroup(DcjUR_o.copy(),
                   DcjUL_o.copy(),
                   DcjL.copy(),
                   DcjR_o.copy())
        V = VGroup(DcjUR_c.copy(),
                   DcjUL_c.copy(),
                   DcjL.copy(),
                   DcjR_c.copy())
        cil0 = Circle(fill_opacity=1) \
            .set_color(WHITE) \
            .scale(20)

        self.wait(1)
        self.play(Write(t0,
                        stroke_color=GREY_C),
                  run_time=2)
        self.play(Write(t0_s,
                        stroke_color=GREY_C),
                  run_time=1)
        self.wait(0.5)
        self.play(Write(t0ss,
                        stroke_color=GREY_C),
                  run_time=1)
        self.play(Write(t0s_s,
                        stroke_color=GREY_C),
                  run_time=1)
        self.wait(1)
        self.play(Uncreate(t0),
                  Uncreate(t0_s),
                  Uncreate(t0ss),
                  Uncreate(t0s_s),
                  run_time=1)
        self.wait(1)
        self.play(ShowCreation(OD_in00),
                  ShowCreation(OD_out),
                  run_time=2)
        self.play(Write(t1,
                        stroke_color=GREY_C),
                  run_time=1)
        self.wait(0.5)
        self.play(Uncreate(t1),
                  run_time=1)
        self.wait(0.5)
        self.play(Write(t1s,
                        stroke_color=GREY_C),
                  run_time=2)
        self.wait(0.5)
        self.play(Uncreate(t1s),
                  run_time=2)
        self.wait(0.5)
        self.play(ShowCreation(cOD_r00),
                  run_time=2)
        self.wait(0.5)
        self.play(Uncreate(cOD_r00),
                  run_time=2)
        self.wait(0.5)
        self.play(ReplacementTransform(OD_in00, OD_in01))
        self.wait(0.5)
        self.play(ShowCreation(cOD_r01),
                  run_time=2)
        self.wait(0.5)
        self.play(Uncreate(cOD_r01),
                  run_time=2)
        self.wait(0.5)
        self.play(ReplacementTransform(OD_in01, OD_in11))
        self.wait(0.5)
        self.play(ShowCreation(cOD_r11),
                  run_time=2)
        self.wait(0.5)
        self.play(Uncreate(cOD_r11),
                  run_time=2)
        self.wait(0.5)
        self.play(Write(t2,
                        stroke_color=GREY_C),
                  run_time=1)
        self.play(DrawBorderThenFill(cil0))

        title1 = Text("如何",
                      font="思源黑体") \
            .shift(np.array([-3.5, 1, 0])).scale(2) \
            .set_color("ff0000")
        title2 = Text("通过", font="思源黑体") \
            .shift(np.array([-1.5, 1, 0])).scale(2) \
            .set_color(ORANGE)
        title3 = Text("多", font="思源黑体") \
            .shift(np.array([0.5, 0.5, 0])).scale(2) \
            .set_color(BLUE_C)
        title4 = Text("个", font="思源黑体") \
            .shift(np.array([1.5, 0.5, 0])).scale(2) \
            .set_color(BLUE_C)
        title5 = Text("开", font="思源黑体") \
            .shift(np.array([2.5, 0.5, 0])).scale(2) \
            .set_color(YELLOW_E)
        title6 = Text("关", font="思源黑体") \
            .shift(np.array([3.5, 0.5, 0])).scale(2) \
            .set_color(GREY_D)
        title7 = Text("控", font="思源黑体") \
            .shift(np.array([-2, -1, 0])).scale(2.5) \
            .set_color(PURPLE)
        title8 = Text("制", font="思源黑体") \
            .shift(np.array([-0.5, -1, 0])).scale(2.5) \
            .set_color(BLUE_C)
        title9 = Text("电", font="思源黑体") \
            .shift(np.array([1, -1.5, 0])) \
            .scale(2) \
            .set_color(ORANGE)
        title10 = Text("路", font="思源黑体") \
            .shift(np.array([2, -1.5, 0])) \
            .scale(2) \
            .set_color(RED_D)
        titleA = Text('How to',
                      gradient=("ff0000", ORANGE)) \
            .shift(np.array([-2.5, 0, 0])) \
            .scale(1.5)
        titleC = Text('Circuit',
                      gradient=(ORANGE, RED_D)) \
            .shift(np.array([1.5, -0.5, 0])) \
            .scale(1.5)
        titleB = Text('Control',
                      gradient=(PURPLE, BLUE)) \
            .shift(np.array([-1.25, -2, 0])) \
            .scale(1.5)
        titleD = Text("With Switch",
                      gradient=(BLUE, PURPLE)) \
            .shift(np.array([2, 1.5, 0])) \
            .scale(1.5)
        titleS = Text("BiliBili  从尽头到开始",
                      t2f={"BiliBili": "Forte", "从尽头到开始": "思源黑体"},
                      slant=ITALIC) \
            .shift(np.array([0, 2.5, 0])) \
            .scale(0.6) \
            .set_color(GREY_D)
        title0 = VGroup(title1, title2, title3,
                        title4, title5, title6, title7,
                        title8, title9, title10, titleA,
                        titleB, titleC, titleD, titleS)

        self.play(ShowCreation(cDL),
                  ShowCreation(cDR),
                  run_time=4)
        self.wait(1)
        self.play(Uncreate(cDL),
                  Uncreate(cDR),
                  run_time=4)
        self.play(ShowCreation(C),
                  run_time=6)
        self.play(C.set_color, GREY_C)
        self.play(ShowCreation(title0),
                  run_time=8)
        self.play(Uncreate(title0),
                  run_time=8)

        t3 = Text("电磁继电器",
                  font="思源黑体",
                  gradient=(BLUE, RED)) \
            .scale(2)
        t3s1 = Text("这是一个电磁继电器",
                    font="思源黑体") \
            .shift(np.array([0, -3.5, 0])) \
            .set_color(GREY_D) \
            .scale(0.5)
        t3s2 = Text("  如果电磁铁状态改变  工作电路相对应的开关也会改变",
                    font="思源黑体") \
            .shift(np.array([0, -3.5, 0])) \
            .set_color(GREY_D) \
            .scale(0.5)
        t4s1 = Text("如果把这个电路的灯泡换成电磁铁",
                    font="思源黑体") \
            .shift(np.array([0, -3.5, 0])) \
            .set_color(GREY_D) \
            .scale(0.5)
        t4s2 = Text("通过电磁铁控制另一个电路的其中一个开关",
                    font="思源黑体") \
            .shift(np.array([0, -3.5, 0])) \
            .set_color(GREY_D) \
            .scale(0.5)
        t4_DRL = D_R_lu_o.copy()
        t4_DR_u = D_R_u.copy()
        t4_DR_d = D_R_d.copy()
        t4_DL_u = D_L_u.copy()
        t4_DL_d = D_L_d.copy()
        t4_D = VGroup(t4_DR_u, t4_DL_d,
                      t4_DR_d, t4_DL_u, t4_DRL) \
            .shift(np.array([-3, 0, 0]))
        t5_DRL_uo = D_R_lu_o.copy()
        t5_DRL_uc = D_R_lu_c.copy()
        t5_DRL_do1 = D_R_ld_o.copy()
        t5_DRL_dc1 = D_R_ld_c.copy()
        t5_DRL_do2 = D_R_ld_o.copy()
        t5_DRL_dc2 = D_R_ld_c.copy()
        t5_DL_u1 = D_L_u.copy()
        t5_DL_d1 = D_L_d.copy()
        t5_DL_u2 = D_L_u.copy().copy()
        t5_DL_d2 = D_L_d.copy().copy()
        t5_D = VGroup(t5_DL_u1, t5_DL_d1,
                      t5_DL_d2, t5_DL_u2,
                      t5_DRL_uo, t5_DRL_uc,
                      t5_DRL_do1, t5_DRL_dc1,
                      t5_DRL_do2, t5_DRL_dc2) \
            .shift(np.array([3, 0, 0]))
        t00_l1 = Line(start=np.array([-1.5, 2.5, 0]),
                      end=np.array([-1.5, 3, 0]))
        t00_l2 = Line(start=np.array([-1.5, 3, 0]),
                      end=np.array([1.5, 3, 0]))
        t00_l3 = Line(start=np.array([1.5, 3, 0]),
                      end=np.array([1.5, 2.1, 0]))
        t00_l = VGroup(t00_l1, t00_l2, t00_l3) \
            .set_color(GREY_C)
        t5 = Text("改变每一个开关的状态",
                  font="思源黑体") \
            .shift(np.array([0, -3.5, 0])) \
            .set_color(GREY_D) \
            .scale(0.5)

        self.play(Write(t3))
        self.wait(2)
        self.play(Uncreate(t3))
        self.play(C.set_color, BLACK)
        self.play(Write(t3s1,
                        stroke_color=GREY_C),
                  run_time=1)
        self.wait(1)
        self.play(Uncreate(t3s1),
                  run_time=1)
        self.play(Write(t3s2,
                        stroke_color=GREY_C),
                  run_time=2)
        self.wait(1)
        self.play(Transform(C, V))
        self.play(Uncreate(t3s2),
                  run_time=1)
        self.play(Uncreate(C),
                  run_time=2)
        self.play(ShowCreation(t4_DRL),
                  ShowCreation(t4_DL_d),
                  run_time=3)
        self.play(Write(t4s1,
                        stroke_color=GREY_C),
                  run_time=1)
        self.play(ReplacementTransform(t4_DRL, t4_DR_u),
                  run_time=1)
        self.play(Uncreate(t4s1),
                  run_time=1)
        self.play(Write(t4s2,
                        stroke_color=GREY_C),
                  run_time=1)
        self.play(ShowCreation(t5_DRL_do1),
                  ShowCreation(t5_DL_u1))
        self.play(Uncreate(t4s2),
                  run_time=1)
        self.play(ShowCreation(t00_l))
        self.play(Write(t5,
                        stroke_color=GREY_C),
                  run_time=1)
        self.wait(1)
        self.play(Uncreate(t5),
                  run_time=1)
        self.play(ReplacementTransform(t4_DL_d, t4_DL_u),
                  ReplacementTransform(t5_DRL_do1, t5_DRL_dc1),
                  ReplacementTransform(t5_DL_u1, t5_DL_d1),
                  ApplyMethod(t00_l.set_color, YELLOW_E),
                  run_time=1.5)
        self.wait(1)
        self.play(ReplacementTransform(t4_DR_u, t4_DR_d),
                  ReplacementTransform(t5_DRL_dc1, t5_DRL_do2),
                  ReplacementTransform(t5_DL_d1, t5_DL_u2),
                  ApplyMethod(t00_l.set_color, GREY_C),
                  run_time=1.5)
        self.wait(1)
        self.play(ReplacementTransform(t5_DRL_do2, t5_DRL_uc),
                  run_time=1.5)

        t6 = Text("同理,使用更多的电磁继电器就可以用更多的开关控制",
                  font="思源黑体") \
            .shift(np.array([0, -3.5, 0])) \
            .set_color(GREY_D) \
            .scale(0.5)

        self.play(Write(t6,
                        stroke_color=GREY_C),
                  run_time=1)
        self.wait(1)
        self.play(Uncreate(t6),
                  run_time=1)
        self.play(ShowCreation(cil0.copy()))

        t7 = Text("使用python在GitHub上的开源项目ManimGL\n音乐是 柳轻颂 - 溯 (钢琴版)\n由bilibili 从尽头到开始创作\n创作过程中没有参考任何教科书外的其他资料",
                  font="思源黑体") \
            .set_color(BLACK) \
            .scale(0.5)
        self.play(Write(t7), run_time=2)

        self.wait(20)
