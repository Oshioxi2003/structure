'use client';
import AboutArea from "@/common/about-area";
import FooterFive from "@/layout/footers/footer-5";
import HeaderSix from "@/layout/headers/header";
import Breadcrumb from "../../common/breadcrumbs/breadcrumb";
import HeroBanner from "../../common/hero-banner";
import CtaArea from "../contact/cta-area";
import TeamArea from "../homes/team-area";
import Brand from "./brand";
import CompanyArea from "./company-area";
import JobArea from "./job-area";
import JourneyArea from "./journey-area";
 
const About = () => {
  return (
    <>
      <HeaderSix />
      <Breadcrumb title_top="About"  title_bottom="OxiTec" />
      <HeroBanner title="About" subtitle="OxiTec" bg_img="/assets/img/breadcrumb/breadcrumb-2.jpg" />
      <Brand />
      <CompanyArea />
      <AboutArea />
      <TeamArea bg_style={true} />
      <JourneyArea />
      <JobArea />
      <CtaArea />
      <FooterFive style_contact={true} style_team={true} />
    </>
  );
};

export default About;
