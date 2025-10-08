'use client';
import FooterFive from "@/layout/footers/footer-5";
import HeaderSeven from "@/layout/headers/header"; 
import SingnInArea from "./singn-in-area";

const SignIn = () => {
  return (
    <>
      <HeaderSeven />
      <SingnInArea />
      <FooterFive style_contact={true} style_team={true} />
    </>
  );
};

export default SignIn;
