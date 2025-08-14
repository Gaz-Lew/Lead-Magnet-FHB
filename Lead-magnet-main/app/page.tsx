import { HeroSection } from "@/components/hero-section"
import { BenefitsSection } from "@/components/benefits-section"
import { GuidePreview } from "@/components/guide-preview"
import { SocialProof } from "@/components/social-proof"
import { LeadCaptureForm } from "@/components/lead-capture-form"
import { Footer } from "@/components/footer"

export default function HomePage() {
  return (
    <main className="min-h-screen">
      <HeroSection />
      <BenefitsSection />
      <GuidePreview />
      <SocialProof />
      <LeadCaptureForm />
      <Footer />
    </main>
  )
}
