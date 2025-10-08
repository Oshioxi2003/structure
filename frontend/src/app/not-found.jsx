"use client";
import Link from "next/link";
import Image from "next/image";
import HeaderFour from "@/layout/headers/header";
import Footer from "@/layout/footers/footer";

// error shapes
import error_shape_1 from "@/assets/img/login/error-shape.png";
import error_shape_2 from "@/assets/img/login/text-404.png";


export const metadata = {
  title: "Oops.! Page Not Found!"
};


export default function NotFoundPage() {
  return (
    <>
      {/* header area start */}
      <HeaderFour style_error={true} />
      {/* header area end */}

      <div id="smooth-wrapper">
        <div id="smooth-content">
          <main>
            <div className="tp-error-area tp-error-ptb p-relative">
              <div className="tp-error-left-shape">
                <Image src={error_shape_1} alt="theme-pure" />
              </div>
              <div className="container">
                <div className="row">
                  <div className="col-xl-12">
                    <div className="tp-error-content-box text-center mb-40">
                      <Image src={error_shape_2} alt="theme-pure" />
                    </div>
                    <div className="tp-error-text-box text-center">
                      <h4 className="error-title-sm">Oops.! Page Not Found!</h4>
                      <p>The page vou are looking for does not exist'</p>
                      <Link
                        className="tp-btn-inner tp-btn-hover alt-color-black"
                        href="/"
                      >
                        <span> Back To Home</span>
                        <b></b>
                      </Link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </main>
          {/* footer area start */}
          <Footer />
          {/* footer area end */}
        </div>
      </div>
    </>
  );
}
