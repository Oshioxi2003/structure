'use client';
import BreadcrumbFour from "@/common/breadcrumbs/breadcrumb-4";
import FooterFive from "@/layout/footers/footer-5";
import HeaderSix from "@/layout/headers/header";
import IntegrationArea from "../homes/integration-area";
import FeatureArea from "../homes/feature-area";

const Integrations = () => {
  return (
    <>
      <HeaderSix />
      <div id="smooth-wrapper">
        <div id="smooth-content">
          <main>
            <BreadcrumbFour />
            <FeatureArea style_integraton={true} />
            <IntegrationArea style_integraton={true}/>
          </main>
          <FooterFive style_contact={true} style_team={true} />
        </div>
      </div>
    </>
  );
};

export default Integrations;
