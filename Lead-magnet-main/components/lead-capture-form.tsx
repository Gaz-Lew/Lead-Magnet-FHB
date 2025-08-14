"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent } from "@/components/ui/card"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import { Label } from "@/components/ui/label"
import { Mail, Lock } from "lucide-react"

export function LeadCaptureForm() {
  const [email, setEmail] = useState("")
  const [firstName, setFirstName] = useState("")
  const [phone, setPhone] = useState("")
  const [propertyStatus, setPropertyStatus] = useState("")
  const [readiness, setReadiness] = useState("")
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [isSubmitted, setIsSubmitted] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsSubmitting(true)

    // Simulate form submission
    await new Promise((resolve) => setTimeout(resolve, 1000))

    setIsSubmitted(true)
    setIsSubmitting(false)
  }

  if (isSubmitted) {
    return (
      <section id="lead-form" className="py-16 bg-gradient-to-br from-asg-gold/10 to-asg-gold/20">
        <div className="container mx-auto px-4 max-w-2xl text-center">
          <Card className="shadow-xl">
            <CardContent className="p-8">
              <div className="bg-asg-gold/20 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-6">
                <Mail className="h-8 w-8 text-asg-gold-dark" />
              </div>
              <h2 className="font-serif text-3xl font-bold text-asg-navy mb-4">Check Your Email!</h2>
              <p className="text-lg text-gray-700 mb-6">
                Your Perth Property Playbook is being sent to <strong>{email || "your inbox"}</strong>
              </p>
              <p className="text-gray-600">
                Don't forget to check your spam folder if you don't see it in the next few minutes.
              </p>
            </CardContent>
          </Card>
        </div>
      </section>
    )
  }

  return (
    <section id="lead-form" className="py-16 bg-gradient-to-br from-asg-gold/10 to-asg-gold/20">
      <div className="container mx-auto px-4 max-w-2xl">
        <Card className="shadow-xl">
          <CardContent className="p-8">
            <div className="text-center mb-8">
              <div className="bg-asg-gold/20 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-6">
                <Mail className="h-8 w-8 text-asg-gold-dark" />
              </div>
              <h2 className="font-serif text-3xl md:text-4xl font-bold text-asg-navy mb-4">Get Your Free Guide Now</h2>
              <p className="text-lg text-gray-700 mb-2">
                Receive the complete Perth Property Playbook via email instantly
              </p>
              <p className="text-sm text-gray-600">
                Join 2,500+ smart property buyers who've already received this guide
              </p>
            </div>

            <form onSubmit={handleSubmit} className="space-y-6">
              <div>
                <Label className="text-base font-medium text-asg-navy mb-3 block">
                  Are you currently renting or own a property?
                </Label>
                <RadioGroup value={propertyStatus} onValueChange={setPropertyStatus} className="flex gap-6">
                  <div className="flex items-center space-x-2">
                    <RadioGroupItem value="renting" id="renting" />
                    <Label htmlFor="renting">Renting</Label>
                  </div>
                  <div className="flex items-center space-x-2">
                    <RadioGroupItem value="own" id="own" />
                    <Label htmlFor="own">Own a property</Label>
                  </div>
                </RadioGroup>
              </div>

              <div>
                <Label className="text-base font-medium text-asg-navy mb-3 block">
                  Are you ready to get into a home right now or just researching?
                </Label>
                <RadioGroup value={readiness} onValueChange={setReadiness} className="flex gap-6">
                  <div className="flex items-center space-x-2">
                    <RadioGroupItem value="ready" id="ready" />
                    <Label htmlFor="ready">Ready to buy now</Label>
                  </div>
                  <div className="flex items-center space-x-2">
                    <RadioGroupItem value="researching" id="researching" />
                    <Label htmlFor="researching">Just researching</Label>
                  </div>
                </RadioGroup>
              </div>

              <div>
                <Input
                  type="text"
                  placeholder="Full Name"
                  value={firstName}
                  onChange={(e) => setFirstName(e.target.value)}
                  required
                  className="h-12 text-lg"
                />
              </div>

              <div>
                <Input
                  type="tel"
                  placeholder="Phone Number"
                  value={phone}
                  onChange={(e) => setPhone(e.target.value)}
                  required
                  className="h-12 text-lg"
                />
              </div>

              <div>
                <Input
                  type="email"
                  placeholder="Email Address (Optional)"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="h-12 text-lg"
                />
              </div>

              <Button
                type="submit"
                disabled={isSubmitting || !firstName || !phone || !propertyStatus || !readiness}
                className="w-full h-12 bg-asg-gold-dark hover:bg-asg-navy text-white text-lg font-semibold rounded-lg shadow-lg hover:shadow-xl transition-all duration-200"
              >
                {isSubmitting ? "Sending..." : "Get Your Free Guide Now"}
                <Mail className="ml-2 h-5 w-5" />
              </Button>
            </form>

            <div className="flex items-center justify-center gap-2 mt-6 text-sm text-gray-600">
              <Lock className="h-4 w-4" />
              <span>Your information is 100% secure and will never be shared</span>
            </div>
          </CardContent>
        </Card>
      </div>
    </section>
  )
}
