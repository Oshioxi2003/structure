"use client";
import BreadcrumbFive from "@/common/breadcrumbs/breadcrumb-5";
import TestimonialArea from "@/common/testimonial-area";
import FooterFive from "@/layout/footers/footer-5";
import HeaderSix from "@/layout/headers/header";
import Brand from "../about/brand";
import CtaArea from "../contact/cta-area";
import FaqArea from "../homes/test/home-2/faq-area";
import PlanArea from "./plan-area";
import PriceArea from "./price-area";

const Price = () => {
  return (
    <>
      <HeaderSix />
      <div id="smooth-wrapper">
        <div id="smooth-content">
          <main>
            <BreadcrumbFive />
            <PriceArea />
            <PlanArea />
            <Brand />
            <TestimonialArea />
            <FaqArea style_service={true} />
            <CtaArea />
          </main>
          <FooterFive style_contact={true} style_team={true} />
        </div>
      </div>
    </>
  );
};

export default Price;
