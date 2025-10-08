export const wowAnimation = () => {
  if (typeof window !== "undefined") {
    import("wow.js").then((module) => {
      const WOW = module.default; // Default export
      new WOW({ live: false }).init();
    });
  }
};
