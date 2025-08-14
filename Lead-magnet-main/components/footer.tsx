export function Footer() {
  return (
    <footer className="bg-asg-navy text-white py-8">
      <div className="container mx-auto px-4 max-w-4xl text-center">
        <div className="flex items-center justify-center gap-3 mb-4">
          <div className="bg-asg-gold text-asg-navy px-3 py-1 rounded font-bold text-lg">ASG</div>
          <span className="text-asg-gold font-medium text-sm uppercase tracking-wide">Amplify Solutions Group</span>
        </div>
        <h3 className="font-serif text-2xl font-bold mb-4 text-asg-gold">Perth Property Playbook</h3>
        <p className="text-gray-300 mb-6">Your trusted guide to smart property buying in Western Australia</p>
        <div className="border-t border-asg-gold/20 pt-6">
          <p className="text-sm text-gray-400">© 2025 Amplify Solutions Group. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}
