'use client';
import ContextProvider from "@/context/ContextProvider";
import FooterFive from "@/layout/footers/footer-5";
import HeaderFive from "@/layout/headers/header";
import BusinessBox from "./business-box";
import CtaArea from "./cta-area";
import FeatureArea from "./feature-area";
import FunFactArea from "./fun-fact-area";
import HeroArea from "./hero-area";
import IntegrationArea from "./integration-area";
import PlanArea from "./plan-area";
import ServiceArea from "./service-area";
import VideoArea from "./video-area";
import AnimateMouse from "./AnimateMouse";
import TestimonialArea from "@/common/testimonial-area";

const HomeOne = () => {
  return (
    <ContextProvider>
      <AnimateMouse />
      <HeaderFive />
      <div id="smooth-wrapper">
        <div id="smooth-content">
          <main className="fix">
            <HeroArea />
            <VideoArea />
            <FunFactArea />
            <ServiceArea />
            <CtaArea />
            <PlanArea />
            <TestimonialArea/>
            <FeatureArea />
            <IntegrationArea />
            <BusinessBox />
          </main>
          <FooterFive bg_style={false} />
        </div>
      </div>
    </ContextProvider>
  );
};

export default HomeOne;
