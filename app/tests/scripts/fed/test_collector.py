import unittest
from unittest import TestCase, mock

from app.scripts.federal_reserve.fomc_collector import (add_to_db,
                                                        check_for_new,
                                                        convert_date, get_data,
                                                        get_new_statement,
                                                        parse_statement)


class test_fomc_collector(TestCase):
    def test_get_data(self) -> None:
        result = get_data()
        self.assertIsInstance(result, list)

    def test_check_for_new(self) -> None:
        with mock.patch('app.models.federal_reserve.database.Fed_Model.fetch') as patched:
            query = "SELECT date FROM fomc_statements ORDER BY id DESC LIMIT 1"
            patched.return_value = "2021-01-15"
            result = check_for_new()
            patched.assert_called_with(query)
            self.assertIsNotNone(result)

    def test_convert_date(self) -> None:
        result = convert_date("4/20/2020 ")
        self.assertEqual(result, "2020-04-20")
        result = convert_date("10/9/2020 ")
        self.assertEqual(result, "2020-10-09")
        result = convert_date("7/2/2010 ")
        self.assertEqual(result, "2010-07-02")

    def test_get_new_statement(self) -> None:
        str_check_for_new = 'app.scripts.federal_reserve.fomc_collector.check_for_new'
        with mock.patch(str_check_for_new) as patched:
            patched.return_value = None
            result = get_new_statement()
            self.assertIsNone(result)

            demo = ["2021-09-22", "https://www.federalreserve.gov/newsevents/pressreleases/monetary20210922a.htm"]
            patched.return_value = demo
            result = get_new_statement()
            self.assertIsNotNone(result)

    def test_parse_statement(self) -> None:
        str_get_new_statement = 'app.scripts.federal_reserve.fomc_collector.get_new_statement'
        with mock.patch(str_get_new_statement) as patched:
            patched.return_value = [p.replace("\n                ", " ") for p in [
                '''The Federal Reserve is committed to using its full range of tools to support the U.S. economy in this challenging
                time, thereby promoting its maximum employment and price stability goals.''',
                '''With progress on vaccinations and strong policy support, indicators of economic activity and employment have
                continued to strengthen. The sectors most adversely affected by the pandemic have improved in recent months, but
                the rise in COVID-19 cases has slowed their recovery. Inflation is elevated, largely reflecting transitory
                factors. Overall financial conditions remain accommodative, in part reflecting policy measures to support the
                economy and the flow of credit to U.S. households and businesses.''',
                '''The path of the economy continues to depend on the course of the virus. Progress on vaccinations will likely
                continue to reduce the effects of the public health crisis on the economy, but risks to the economic outlook
                remain.''',
                '''The Committee seeks to achieve maximum employment and inflation at the rate of 2 percent over the longer run.
                With inflation having run persistently below this longer-run goal, the Committee will aim to achieve inflation
                moderately above 2 percent for some time so that inflation averages 2 percent over time and longerâ\x80\x91term
                inflation expectations remain well anchored at 2 percent. The Committee expects to maintain an accommodative
                stance of monetary policy until these outcomes are achieved. The Committee decided to keep the target range for
                the federal funds rate at 0 to 1/4 percent and expects it will be appropriate to maintain this target range until
                labor market conditions have reached levels consistent with the Committee's assessments of maximum employment and
                inflation has risen to 2 percent and is on track to moderately exceed 2 percent for some time. Last December, the
                Committee indicated that it would continue to increase its holdings of Treasury securities by at least $80
                billion per month and of agency mortgageâ\x80\x91backed securities by at least $40 billion per month until
                substantial further progress has been made toward its maximum employment and price stability goals. Since then,
                the economy has made progress toward these goals. If progress continues broadly as expected, the Committee judges
                that a moderation in the pace of asset purchases may soon be warranted. These asset purchases help foster smooth
                market functioning and accommodative financial conditions, thereby supporting the flow of credit to households
                and businesses.''',
                '''In assessing the appropriate stance of monetary policy, the Committee will continue to monitor the
                implications of incoming information for the economic outlook. The Committee would be prepared to adjust the
                stance of monetary policy as appropriate if risks emerge that could impede the attainment of the Committee's
                goals. The Committee's assessments will take into account a wide range of information, including readings on
                public health, labor market conditions, inflation pressures and inflation expectations, and financial and
                international developments.''',
                '''Voting for the monetary policy action were Jerome H. Powell, Chair; John C. Williams, Vice Chair; Thomas I.
                Barkin; Raphael W. Bostic; Michelle W. Bowman; Lael Brainard; Richard H. Clarida; Mary C. Daly; Charles L. Evans;
                Randal K. Quarles; and Christopher J. Waller.''',
            ]]
            expected = "The Federal Reserve is committed to using its full range of tools to support the U.S. economy in this challenging time, thereby promoting its maximum employment and price stability goals.\n\n      With progress on vaccinations and strong policy support, indicators of economic activity and employment have continued to strengthen. The sectors most adversely affected by the pandemic have improved in recent months, but the rise in COVID-19 cases has slowed their recovery. Inflation is elevated, largely reflecting transitory factors. Overall financial conditions remain accommodative, in part reflecting policy measures to support the economy and the flow of credit to U.S. households and businesses.\n      \n      The path of the economy continues to depend on the course of the virus. Progress on vaccinations will likely continue to reduce the effects of the public health crisis on the economy, but risks to the economic outlook remain.\n      \n      The Committee seeks to achieve maximum employment and inflation at the rate of 2 percent over the longer run. With inflation having run persistently below this longer-run goal, the Committee will aim to achieve inflation moderately above 2 percent for some time so that inflation averages 2 percent over time and longer term inflation expectations remain well anchored at 2 percent. The Committee expects to maintain an accommodative stance of monetary policy until these outcomes are achieved. The Committee decided to keep the target range for the federal funds rate at 0 to 1/4 percent and expects it will be appropriate to maintain this target range until labor market conditions have reached levels consistent with the Committee's assessments of maximum employment and inflation has risen to 2 percent and is on track to moderately exceed 2 percent for some time. Last December, the Committee indicated that it would continue to increase its holdings of Treasury securities by at least $80 billion per month and of agency mortgage backed securities by at least $40 billion per month until substantial further progress has been made toward its maximum employment and price stability goals. Since then, the economy has made progress toward these goals. If progress continues broadly as expected, the Committee judges that a moderation in the pace of asset purchases may soon be warranted. These asset purchases help foster smooth market functioning and accommodative financial conditions, thereby supporting the flow of credit to households and businesses.\n      \n      In assessing the appropriate stance of monetary policy, the Committee will continue to monitor the implications of incoming information for the economic outlook. The Committee would be prepared to adjust the stance of monetary policy as appropriate if risks emerge that could impede the attainment of the Committee's goals. The Committee's assessments will take into account a wide range of information, including readings on public health, labor market conditions, inflation pressures and inflation expectations, and financial and international developments.\n      \n      Voting for the monetary policy action were Jerome H. Powell, Chair; John C. Williams, Vice Chair; Thomas I. Barkin; Raphael W. Bostic; Michelle W. Bowman; Lael Brainard; Richard H. Clarida; Mary C. Daly; Charles L. Evans; Randal K. Quarles; and Christopher J. Waller."  # noqa: E501
            result = parse_statement()
            self.maxDiff = None
            self.assertEqual(result, expected)

    def test_add_to_db(self):
        str_check_for_new = "app.scripts.federal_reserve.fomc_collector.check_for_new"
        with mock.patch(str_check_for_new) as patched:
            patched.return_value = None
            result = add_to_db()
            self.assertIsNone(result)

            url_base = "https://www.federalreserve.gov/"
            url_end = "newsevents/pressreleases/monetary20210922a.htm"
            patched.return_value = ["2021-09-22", f"{url_base + url_end}"]
            fed_model_exec_many = "app.models.federal_reserve.database.Fed_Model.executemany"
            with mock.patch(fed_model_exec_many) as exec_many_patched:
                add_to_db()
                expected_query = "INSERT INTO fomc_statements (date,year,statement) VALUES (%s,%s,%s)"
                expected_data = [(
                    "2021-09-22", "2021",
                    "The Federal Reserve is committed to using its full range of tools to support the U.S. economy in this challenging time, thereby promoting its maximum employment and price stability goals.\n\n      With progress on vaccinations and strong policy support, indicators of economic activity and employment have continued to strengthen. The sectors most adversely affected by the pandemic have improved in recent months, but the rise in COVID-19 cases has slowed their recovery. Inflation is elevated, largely reflecting transitory factors. Overall financial conditions remain accommodative, in part reflecting policy measures to support the economy and the flow of credit to U.S. households and businesses.\n      \n      The path of the economy continues to depend on the course of the virus. Progress on vaccinations will likely continue to reduce the effects of the public health crisis on the economy, but risks to the economic outlook remain.\n      \n      The Committee seeks to achieve maximum employment and inflation at the rate of 2 percent over the longer run. With inflation having run persistently below this longer-run goal, the Committee will aim to achieve inflation moderately above 2 percent for some time so that inflation averages 2 percent over time and longer term inflation expectations remain well anchored at 2 percent. The Committee expects to maintain an accommodative stance of monetary policy until these outcomes are achieved. The Committee decided to keep the target range for the federal funds rate at 0 to 1/4 percent and expects it will be appropriate to maintain this target range until labor market conditions have reached levels consistent with the Committee's assessments of maximum employment and inflation has risen to 2 percent and is on track to moderately exceed 2 percent for some time. Last December, the Committee indicated that it would continue to increase its holdings of Treasury securities by at least $80 billion per month and of agency mortgage backed securities by at least $40 billion per month until substantial further progress has been made toward its maximum employment and price stability goals. Since then, the economy has made progress toward these goals. If progress continues broadly as expected, the Committee judges that a moderation in the pace of asset purchases may soon be warranted. These asset purchases help foster smooth market functioning and accommodative financial conditions, thereby supporting the flow of credit to households and businesses.\n      \n      In assessing the appropriate stance of monetary policy, the Committee will continue to monitor the implications of incoming information for the economic outlook. The Committee would be prepared to adjust the stance of monetary policy as appropriate if risks emerge that could impede the attainment of the Committee's goals. The Committee's assessments will take into account a wide range of information, including readings on public health, labor market conditions, inflation pressures and inflation expectations, and financial and international developments.\n      \n      Voting for the monetary policy action were Jerome H. Powell, Chair; John C. Williams, Vice Chair; Thomas I. Barkin; Raphael W. Bostic; Michelle W. Bowman; Lael Brainard; Richard H. Clarida; Mary C. Daly; Charles L. Evans; Randal K. Quarles; and Christopher J. Waller.",  # noqa: E501
                )]
                exec_many_patched.assert_called_with(expected_query, expected_data)


if __name__ == '__main__':
    unittest.main()
