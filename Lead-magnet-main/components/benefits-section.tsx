import { Card, CardContent } from "@/components/ui/card"
import { Home, TrendingUp, MapPin, Calculator } from "lucide-react"

const benefits = [
  {
    icon: Home,
    title: "First Home Buyer Secrets",
    description:
      "Navigate grants, loans, and hidden costs with confidence. Avoid the common mistakes that cost buyers thousands.",
  },
  {
    icon: TrendingUp,
    title: "Investment Strategies",
    description:
      "Learn which Perth suburbs offer the best growth potential and rental yields for building long-term wealth.",
  },
  {
    icon: MapPin,
    title: "Suburb Selection Matrix",
    description: "Our exclusive scoring system helps you identify undervalued areas before they boom.",
  },
  {
    icon: Calculator,
    title: "Financial Planning Tools",
    description: "Calculate borrowing capacity, stamp duty, and ongoing costs with our proven formulas.",
  },
]

export function BenefitsSection() {
  return (
    <section className="py-16 bg-white">
      <div className="container mx-auto px-4 max-w-6xl">
        <div className="text-center mb-12">
          <h2 className="font-serif text-3xl md:text-4xl font-bold text-asg-navy mb-4">What You'll Discover Inside</h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            This comprehensive guide contains the strategies and insights that have helped thousands of buyers make
            smart property decisions in Perth.
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-6">
          {benefits.map((benefit, index) => (
            <Card key={index} className="border-2 border-gray-100 hover:border-asg-gold transition-colors duration-200">
              <CardContent className="p-6">
                <div className="flex items-start gap-4">
                  <div className="bg-asg-gold/20 p-3 rounded-lg">
                    <benefit.icon className="h-6 w-6 text-asg-gold-dark" />
                  </div>
                  <div>
                    <h3 className="font-semibold text-lg text-asg-navy mb-2">{benefit.title}</h3>
                    <p className="text-gray-600">{benefit.description}</p>
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  )
}
