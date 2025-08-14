"use client"

import { Button } from "@/components/ui/button"
import { ArrowDown } from "lucide-react"
import Image from "next/image"

export function HeroSection() {
  const scrollToForm = () => {
    document.getElementById("lead-form")?.scrollIntoView({ behavior: "smooth" })
  }

  return (
    <section className="relative bg-gradient-to-br from-asg-gold/20 to-asg-gold/40 py-16 md:py-24 overflow-hidden">
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute top-0 right-0 w-96 h-96 bg-asg-purple/10 transform rotate-45 translate-x-48 -translate-y-48"></div>
        <div className="absolute bottom-0 left-0 w-64 h-64 bg-asg-navy/10 transform rotate-12 -translate-x-32 translate-y-32"></div>
      </div>

      <div className="container mx-auto px-4 max-w-4xl text-center relative z-10">
        <div className="mb-8">
          <div className="flex items-center justify-center mb-4">
            <Image src="/asg-logo.png" alt="Amplify Solutions Group" width={200} height={60} className="h-12 w-auto" />
          </div>
          <span className="inline-block bg-asg-gold text-asg-navy px-4 py-2 rounded-full text-sm font-medium">
            FREE DOWNLOAD • 2025 EDITION
          </span>
        </div>

        <h1 className="font-serif text-4xl md:text-6xl font-bold text-asg-navy mb-6 leading-tight">
          Perth Property Playbook
        </h1>

        <p className="text-xl md:text-2xl text-gray-700 mb-8 font-medium">
          Your Step-by-Step Guide to Buying Smart in Western Australia
        </p>

        <div className="bg-white/90 backdrop-blur-sm rounded-lg p-6 md:p-8 mb-8 shadow-lg border border-asg-gold/20">
          <p className="text-lg text-gray-800 mb-4">
            From first home to investment portfolio – discover the insider strategies that successful Perth property
            buyers use to make informed decisions in today's market.
          </p>

          <div className="flex flex-wrap justify-center gap-4 text-sm text-gray-600">
            <span className="flex items-center gap-1">✓ Market Analysis & Trends</span>
            <span className="flex items-center gap-1">✓ Suburb Selection Guide</span>
            <span className="flex items-center gap-1">✓ Investment Strategies</span>
          </div>
        </div>

        <Button
          onClick={scrollToForm}
          size="lg"
          className="bg-asg-gold-dark hover:bg-asg-navy text-white px-8 py-4 text-lg font-semibold rounded-lg shadow-lg hover:shadow-xl transition-all duration-200"
        >
          Get Your Free Guide Now
          <ArrowDown className="ml-2 h-5 w-5" />
        </Button>

        <p className="text-sm text-gray-600 mt-4">
          No spam. Unsubscribe anytime. Trusted by 2,500+ Perth property buyers.
        </p>
      </div>
    </section>
  )
}
