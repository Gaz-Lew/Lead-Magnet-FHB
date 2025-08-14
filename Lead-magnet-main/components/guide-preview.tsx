import { Card, CardContent } from "@/components/ui/card"

const chapters = [
  "Chapter 1: Perth Market Overview & 2025 Trends",
  "Chapter 2: First Home Buyer's Complete Checklist",
  "Chapter 3: The Suburb Selection Framework",
  "Chapter 4: Investment Property Strategies",
  "Chapter 5: Financing & Government Grants Guide",
  "Chapter 6: Negotiation Tactics That Work",
  "Chapter 7: Due Diligence & Inspection Checklist",
  "Chapter 8: Building Your Property Portfolio",
]

export function GuidePreview() {
  return (
    <section className="py-16 bg-gray-50">
      <div className="container mx-auto px-4 max-w-4xl">
        <div className="text-center mb-12">
          <h2 className="font-serif text-3xl md:text-4xl font-bold text-gray-900 mb-4">Complete Table of Contents</h2>
          <p className="text-lg text-gray-600">
            8 comprehensive chapters covering everything you need to know about buying property in Perth
          </p>
        </div>

        <Card className="shadow-lg">
          <CardContent className="p-8">
            <div className="grid gap-4">
              {chapters.map((chapter, index) => (
                <div key={index} className="flex items-center gap-4 p-4 bg-white rounded-lg border border-gray-100">
                  <div className="bg-orange-600 text-white rounded-full w-8 h-8 flex items-center justify-center font-semibold text-sm">
                    {index + 1}
                  </div>
                  <span className="text-gray-800 font-medium">{chapter}</span>
                </div>
              ))}
            </div>

            <div className="mt-8 p-6 bg-amber-50 rounded-lg border border-amber-200">
              <h3 className="font-semibold text-lg text-gray-900 mb-2">Bonus Materials Included:</h3>
              <ul className="text-gray-700 space-y-1">
                <li>• Suburb comparison spreadsheet template</li>
                <li>• Property inspection checklist (printable PDF)</li>
                <li>• Mortgage broker contact list</li>
                <li>• Government grants eligibility calculator</li>
              </ul>
            </div>
          </CardContent>
        </Card>
      </div>
    </section>
  )
}
